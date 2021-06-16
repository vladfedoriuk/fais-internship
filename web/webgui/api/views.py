from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from .serializers import get_serializer, ReleaseSerializer, FilesSerializer
from django.apps import apps
from core.models import Configuration, Files, Release
from . import utils
from .utils import exceptions
from .utils.codes import ResponseData
from rest_framework import status
from collections import defaultdict
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from rest_framework.serializers import ValidationError
from itertools import groupby
from operator import attrgetter


version_param = openapi.Parameter(
    name="version",
    in_=openapi.IN_QUERY,
    description="The version of the parameters.",
    type=openapi.TYPE_INTEGER,
)

token_header = openapi.Parameter(
    name="Authorization",
    in_=openapi.IN_HEADER,
    description="Token <token>",
    type=openapi.TYPE_STRING,
)

class UtilsMixIn:
    @staticmethod
    def get_run(run_id):
        try:
            run = Files.objects.get(run_id=run_id)
        except Files.DoesNotExist:
            raise utils.exceptions.InvalidRunId(
                detail=f"The run with run_id={run_id} was not found.")
        except Files.MultipleObjectsReturned:
            raise utils.exceptions.InvalidRunId(
                detail=f"There are more than one run with run_id={run_id}"
            )
        return run
    
    @staticmethod
    def check_version(version):
        try:
            version = int(version)
            if version < 1:
                raise ValueError
        except (ValueError, TypeError):
            raise utils.exceptions.InvalidVersion
    
    @staticmethod
    def response_from_api_exception(e):
        return Response(
            data=ResponseData(
                http_status=e.status_code,
                code=getattr(
                    utils.codes, 
                    f'CODE_{e.status_code}'
                )._asdict(),
                message=e.detail,
                errors=[repr(e)],
                data=None,
            )._asdict(),
            status=e.status_code,
        )
        

class LatestConfigurationValidityDatesForRunMinMaxView(UtilsMixIn, APIView):

    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[version_param, token_header],
        responses={
            404: utils.codes.CODE_404.text,
            401: utils.codes.CODE_401.text,
            204: utils.codes.CODE_204.text,
            200: utils.codes.CODE_200.text,
        },
    )
    def get(self, request, min_run_id, max_run_id):
        core_models = apps.get_app_config("core").get_models()
        core_models = list(filter(lambda x: issubclass(x, Configuration), core_models))

        try:
            run_min = self.get_run(run_id=min_run_id)
            run_max = self.get_run(run_id=max_run_id)
        except utils.exceptions.InvalidRunId as e:
            return self.response_from_api_exception(e)
            
        version = request.query_params.get("version")
        if version:
            try:
                self.check_version(version)
            except utils.exceptions.InvalidVersion as e:
                return self.response_from_api_exception(e)

        conf_json = defaultdict(list)
        for conf_model in core_models:
            confs = conf_model.objects.filter(
                valid_from__gte=run_min.start_time, valid_to__lte=run_max.stop_time
            )
            if version:
                confs = confs.filter(version=version)

            if not confs:
                return Response(
                    data=ResponseData(
                        http_status=status.HTTP_204_NO_CONTENT,
                        code=utils.codes.CODE_204._asdict(),
                        message="Some of the configuration parameters do not exist.",
                        errors=[],
                        data=None,
                    )._asdict(),
                    status=status.HTTP_204_NO_CONTENT,
                )

            conf_json[conf_model.__class__.__name__].extend(confs)

        if not conf_json:
            return Response(
                data=ResponseData(
                    http_status=status.HTTP_204_NO_CONTENT,
                    code=utils.codes.CODE_204._asdict(),
                    message="OK.",
                    errors=[],
                    data=None,
                )._asdict(),
                status=status.HTTP_204_NO_CONTENT,
            )

        confs = next(iter(conf_json.values()))
        res = []
        for _, g in groupby(confs, key=attrgetter("valid_from")):
            max_version = max(g, key=attrgetter("version"))
            res.append(
                {"valid_from": max_version.valid_from, "valid_to": max_version.valid_to}
            )

        return Response(
            data=ResponseData(
                http_status=status.HTTP_200_OK,
                code=utils.codes.CODE_200._asdict(),
                message="OK",
                errors=[],
                data=res,
            )._asdict(),
            status=status.HTTP_200_OK,
        )


class LatestConfigurationValidityDatesForRunView(UtilsMixIn, APIView):

    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[version_param, token_header],
        responses={
            404: utils.codes.CODE_404.text,
            401: utils.codes.CODE_401.text,
            204: utils.codes.CODE_204.text,
            200: utils.codes.CODE_200.text,
        },
    )
    def get(self, request, run_id):
        core_models = apps.get_app_config("core").get_models()
        core_models = list(filter(lambda x: issubclass(x, Configuration), core_models))

        try:
            run = self.get_run(run_id=run_id)
        except utils.exceptions.InvalidRunId as e:
            return self.response_from_api_exception(e)

        version = request.query_params.get("version")
        if version:
            try:
                self.check_version(version)
            except utils.exceptions.InvalidVersion as e:
                return self.response_from_api_exception(e)
            
        conf_json = defaultdict(list)
        for conf_model in core_models:
            confs = conf_model.objects.filter(
                valid_from__lte=run.start_time, valid_to__gte=run.stop_time
            ).all()

            if version:
                confs = confs.filter(version=version)

            if not confs:
                return Response(
                    data=ResponseData(
                        http_status=status.HTTP_204_NO_CONTENT,
                        code=utils.codes.CODE_204._asdict(),
                        message="Some of the configuration parameters do not exist.",
                        errors=[],
                        data=None,
                    )._asdict(),
                    status=status.HTTP_204_NO_CONTENT,
                )

            conf_json[conf_model.__class__.__name__].extend(confs)

        if not conf_json:
            return Response(
                data=ResponseData(
                    http_status=status.HTTP_204_NO_CONTENT,
                    code=utils.codes.CODE_204._asdict(),
                    message="OK.",
                    errors=[],
                    data=None,
                )._asdict(),
                status=status.HTTP_204_NO_CONTENT,
            )

        confs = next(iter(conf_json.values()))
        max_id, max_valid_from, _ = max(
            ((i, x.valid_from, version) for i, x in enumerate(confs)),
            key=lambda x: tuple(x[1:]),
        )
        max_valid_to = confs[max_id].valid_to
        return Response(
            data=ResponseData(
                http_status=status.HTTP_200_OK,
                code=utils.codes.CODE_200._asdict(),
                message="OK",
                errors=[],
                data={
                    "valid_from": max_valid_from.strftime("%Y-%m-%dT%H:%M"),
                    "valid_to": max_valid_to.strftime("%Y-%m-%dT%H:%M"),
                    "run_id": run_id,
                },
            )._asdict(),
            status=status.HTTP_200_OK,
        )


class ConfigurationsForRunView(UtilsMixIn, APIView):

    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[version_param, token_header],
        responses={
            404: utils.codes.CODE_404.text,
            401: utils.codes.CODE_401.text,
            204: utils.codes.CODE_204.text,
            200: utils.codes.CODE_200.text,
        },
    )
    def get(self, request, run_id):
        core_models = apps.get_app_config("core").get_models()
        core_models = list(filter(lambda x: issubclass(x, Configuration), core_models))

        try:
            run = self.get_run(run_id=run_id)
        except utils.exceptions.InvalidRunId as e:
            return self.response_from_api_exception(e)

        version = request.query_params.get("version")
        if version:
            try:
                self.check_version(version)
            except utils.exceptions.InvalidVersion as e:
                return self.response_from_api_exception(e)
            
        conf_json = defaultdict(list)
        for conf_model in core_models:
            serializer = get_serializer(conf_model)
            confs = conf_model.objects.filter(
                valid_from__lte=run.start_time, valid_to__gte=run.stop_time
            ).all()
            confs = serializer(confs, many=True)

            if version:
                versions = [x["version"] for x in confs.data]

                if version not in versions:
                    return Response(
                        data=ResponseData(
                            http_status=status.HTTP_404_NOT_FOUND,
                            code=utils.codes.CODE_404._asdict(),
                            message=f"The version {version} was not found in one or more of the tables.",
                            errors=[],
                            data=None,
                        )._asdict(),
                        status=status.HTTP_404_NOT_FOUND,
                    )
                else:
                    confs = [x for x in confs.data if x["version"] == version]
            else:
                confs = [x for x in confs.data]

            if not confs:
                return Response(
                    data=ResponseData(
                        http_status=status.HTTP_204_NO_CONTENT,
                        code=utils.codes.CODE_204._asdict(),
                        message="Some of the configuration parameters do not exist.",
                        errors=[],
                        data=None,
                    )._asdict(),
                    status=status.HTTP_204_NO_CONTENT,
                )

            conf_json[serializer.model_name()].extend(confs)

        if not conf_json:
            return Response(
                data=ResponseData(
                    http_status=status.HTTP_204_NO_CONTENT,
                    code=utils.codes.CODE_204._asdict(),
                    message="OK.",
                    errors=[],
                    data=None,
                )._asdict(),
                status=status.HTTP_204_NO_CONTENT,
            )

        return Response(
            data=ResponseData(
                http_status=status.HTTP_200_OK,
                code=utils.codes.CODE_200._asdict(),
                message="OK",
                errors=[],
                data=conf_json,
            )._asdict(),
            status=status.HTTP_200_OK,
        )


class ConfigurationsForReleaseView(UtilsMixIn, APIView):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[version_param, token_header],
        responses={
            404: utils.codes.CODE_404.text,
            401: utils.codes.CODE_401.text,
            204: utils.codes.CODE_204.text,
            200: utils.codes.CODE_200.text,
        },
    )
    def get(self, request, release_name):
        try:
            release = Release.objects.get(name=release_name)
        except Release.DoesNotExist as e:
            return Response(
                data=ResponseData(
                    http_status=status.HTTP_404_NOT_FOUND,
                    code=utils.codes.CODE_404._asdict(),
                    message=f"The release with name={release_name} was not found.",
                    errors=[repr(e)],
                    data=None,
                )._asdict(),
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            core_models = apps.get_app_config("core").get_models()
            core_models = list(
                filter(lambda x: issubclass(x, Configuration), core_models)
            )

            version = request.query_params.get("version")
            if version:
                try:
                    self.check_version(version)
                except utils.exceptions.InvalidVersion as e:
                    return self.response_from_api_exception(e)

            conf_json = defaultdict(list)
            for conf_model in core_models:
                serializer = get_serializer(conf_model)
                confs = getattr(
                    release, f"{conf_model.__name__.lower()}_versions", None
                )
                if not confs:
                    return Response(
                        data=ResponseData(
                            http_status=status.HTTP_204_NO_CONTENT,
                            code=utils.codes.CODE_204._asdict(),
                            message=f"""
                            None of versions of {conf_model.__name__} 
                            has been assigned to a release {release_name}
                            """,
                            errors=[],
                            data=None,
                        )._asdict(),
                        status=status.HTTP_204_NO_CONTENT,
                    )

                confs = serializer(confs, many=True)

                if version:
                    versions = [x["version"] for x in confs.data]
                    if version not in versions:
                        return Response(
                            data=ResponseData(
                                http_status=status.HTTP_404_NOT_FOUND,
                                code=utils.codes.CODE_404._asdict(),
                                message=f"The version {version} was not found in one or more of the tables.",
                                errors=[],
                                data=None,
                            )._asdict(),
                            status=status.HTTP_404_NOT_FOUND,
                        )
                    else:
                        confs = [x for x in confs.data if x["version"] == version]
                else:
                    confs = [x for x in confs.data]

                if not confs:
                    return Response(
                        data=ResponseData(
                            http_status=status.HTTP_204_NO_CONTENT,
                            code=utils.codes.CODE_204._asdict(),
                            message="Some of the configuration parameters do not exist.",
                            errors=[],
                            data=None,
                        )._asdict(),
                        status=status.HTTP_204_NO_CONTENT,
                    )

                conf_json[serializer.model_name()].extend(confs)

            if not conf_json:
                return Response(
                    data=ResponseData(
                        http_status=status.HTTP_204_NO_CONTENT,
                        code=utils.codes.CODE_204._asdict(),
                        message="OK.",
                        errors=[],
                        data=None,
                    )._asdict(),
                    status=status.HTTP_204_NO_CONTENT,
                )

            return Response(
                data=ResponseData(
                    http_status=status.HTTP_200_OK,
                    code=utils.codes.CODE_200._asdict(),
                    message="OK",
                    errors=[],
                    data=conf_json,
                )._asdict(),
                status=status.HTTP_200_OK,
            )


class ConfigurationsForRunMinMaxView(UtilsMixIn, APIView):

    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    

    @swagger_auto_schema(
        manual_parameters=[version_param, token_header],
        responses={
            404: utils.codes.CODE_404.text,
            401: utils.codes.CODE_401.text,
            204: utils.codes.CODE_204.text,
            200: utils.codes.CODE_200.text,
        },
    )
    def get(self, request, min_run_id, max_run_id):
        core_models = apps.get_app_config("core").get_models()
        core_models = list(filter(lambda x: issubclass(x, Configuration), core_models))

        try:
            run_min = self.get_run(run_id=min_run_id)
            run_max = self.get_run(run_id=max_run_id)
        except utils.exceptions.InvalidRunId as e:
            return self.response_from_api_exception(e)
           
        version = request.query_params.get("version")
        if version:
            try:
                self.check_version(version)
            except utils.exceptions.InvalidVersion as e:
                return self.response_from_api_exception(e)

        conf_json = defaultdict(list)
        for conf_model in core_models:
            serializer = get_serializer(conf_model)
            confs = conf_model.objects.filter(
                valid_from__gte=run_min.start_time, valid_to__lte=run_max.stop_time
            )
            if version:
                confs = confs.filter(version=version)

            confs = serializer(confs.all(), many=True)
            if not confs.data:
                return Response(
                    data=ResponseData(
                        http_status=status.HTTP_204_NO_CONTENT,
                        code=utils.codes.CODE_204._asdict(),
                        message="Some of the configuration parameters do not exist.",
                        errors=[],
                        data=None,
                    )._asdict(),
                    status=status.HTTP_204_NO_CONTENT,
                )

            conf_json[serializer.model_name()].extend(confs.data)

        if not conf_json:
            return Response(
                data=ResponseData(
                    http_status=status.HTTP_204_NO_CONTENT,
                    code=utils.codes.CODE_204._asdict(),
                    message="OK.",
                    errors=[],
                    data=None,
                )._asdict(),
                status=status.HTTP_204_NO_CONTENT,
            )

        return Response(
            data=ResponseData(
                http_status=status.HTTP_200_OK,
                code=utils.codes.CODE_200._asdict(),
                message="OK",
                errors=[],
                data=conf_json,
            )._asdict(),
            status=status.HTTP_200_OK,
        )


class ConfigurationRetrieveView(UtilsMixIn, ListModelMixin, GenericAPIView):

    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def get_model(self, name):
        try:
            model_class = apps.get_app_config("core").get_model(name)
        except LookupError:
            raise utils.exceptions.InvalidConfigurationName
        return model_class
        
    def get_queryset(self):
        conf_name = self.kwargs["name"]
        conf_model = self.get_model(conf_name)
        return conf_model.objects.all()

    def get_serializer_class(self):
        conf_name = self.kwargs["name"]
        conf_model = self.get_model(conf_name)
        return get_serializer(conf_model)

    def filter_queryset(self, queryset):
        run = self.get_run(self.kwargs["run_id"])
        version = self.request.query_params.get("version")
        new_queryset = queryset.filter(
            valid_from__lte=run.start_time, valid_to__gte=run.stop_time
        )
        if version:
            self.check_version(version)
            new_queryset = new_queryset.filter(version=version)
        if not new_queryset.exists():
            raise utils.exceptions.EmptyQueryset
        return new_queryset

    @swagger_auto_schema(
        manual_parameters=[version_param, token_header],
        responses={
            404: utils.codes.CODE_404.text,
            401: utils.codes.CODE_401.text,
            204: utils.codes.CODE_204.text,
            200: utils.codes.CODE_200.text,
        },
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FilesCreateView(CreateModelMixin, GenericAPIView):

    serializer_class = FilesSerializer

    def get_queryset(self):
        return Files.objects.all()

    def perform_create(self, serializer):
        try:
            serializer.save(file_name=str(None))
        except Exception as e:
            raise ValidationError(e)

    @swagger_auto_schema(request_body=FilesSerializer, responses={201: FilesSerializer})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
