from django.test import TestCase
from rest_framework import status
from rest_framework.test import (
    APITestCase,
    APIClient,
    force_authenticate,
    APIRequestFactory,
)
from rest_framework.authtoken.models import Token
from django.urls import include, path, reverse
from django.contrib.auth.models import User
from django.conf import settings
from core.models import Release, Files, Configuration
from datetime import datetime
from django.apps import apps
from api.serializers import get_serializer
from api.views import ConfigurationRetrieveView
import random

import os
import pytz

from interact.scripts.parser import write_to_database


class ApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username=settings.DEFAULT_ADMIN.get("username"),
            password=settings.DEFAULT_ADMIN.get("password"),
            email=settings.DEFAULT_ADMIN.get("email"),
            is_active=True,
            is_superuser=True,
            is_staff=True,
        )
        self.user.save()
        Token.objects.get_or_create(user=self.user)
        release = Release(name="test-release")
        release.save()
        self.release = release
        write_to_database(
            conf_file_path=os.path.join(os.path.dirname(__file__), "test_conf.txt"),
            release=release,
            version=1,
            valid_from=datetime(2021, 12, 20, 18, 30, tzinfo=pytz.UTC),
            valid_to=datetime(2021, 12, 21, 16, 40, tzinfo=pytz.UTC),
        )
        self.client = APIClient()
        self.factory = APIRequestFactory()
        run = Files(
            file_name="test-run",
            run_id=1,
            start_time=datetime(2021, 12, 20, 19, 30, tzinfo=pytz.UTC),
            stop_time=datetime(2021, 12, 20, 20, 30, tzinfo=pytz.UTC),
        )
        run.save()
        self.run = run
        self.param_models = list(
            filter(
                lambda x: issubclass(x, Configuration),
                apps.get_app_config("core").get_models(),
            )
        )

    def test_auth_token_retrieval(self):
        auth_url = reverse("api:token_for_user")
        response = self.client.post(
            auth_url,
            {
                "username": settings.DEFAULT_ADMIN.get("username"),
                "password": settings.DEFAULT_ADMIN.get("password"),
            },
            format="json",
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        token = Token.objects.get(user=self.user)
        self.assertEqual(str(token), response.data.get("token"))
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        retrieve_url = reverse("api:conf_for_run", kwargs={"run_id": 1})
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_for_release(self):
        release_url = reverse("api:conf_for_release", args=[self.release.name])
        response = self.client.get(release_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(user=self.user, token=self.user.auth_token)
        response = self.client.get(release_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        model = random.choice(self.param_models)
        params = response.data["data"][model.__name__][0]
        serializer = get_serializer(model)
        serialized_data = serializer(model._default_manager.first())
        self.assertEqual(params, serialized_data.data)

    def test_retrieve_for_name_run(self):
        token = Token.objects.get(user=self.user)
        for model in self.param_models:
            args = [model.__name__, 1]
            url = reverse("api:params_for_class", args=args)
            request = self.factory.get(url)
            force_authenticate(request, user=self.user, token=token)
            view = ConfigurationRetrieveView.as_view()
            response = view(request, **dict(zip(("name", "run_id"), args)))
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_validity_latest(self):
        for model in self.param_models:
            url = reverse("api:latest_validity_for_run", args=[1])
            self.client.force_authenticate(user=self.user)
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_run_add(self):
        run_url = reverse("api:runs_create")
        self.client.force_authenticate(user=self.user, token=self.user.auth_token)
        response = self.client.post(
            run_url,
            {
                "start_time": datetime(2021, 12, 23, 12, 20, tzinfo=pytz.UTC),
                "stop_time": datetime(2021, 12, 25, 15, 40, tzinfo=pytz.UTC),
                "run_id": 2,
            },
        )
        self.assertEqual(response.status_code, 201),
        self.assertEqual(Files._default_manager.count(), 2)
