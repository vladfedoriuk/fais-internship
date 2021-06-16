from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

app_name = "api"

urlpatterns = [
    path(
        "retrieve/<int:run_id>/",
        views.ConfigurationsForRunView.as_view(),
        name="conf_for_run",
    ),
    path(
        "retrieve/release/<slug:release_name>/",
        views.ConfigurationsForReleaseView.as_view(),
        name="conf_for_release",
    ),
    path(
        "retrieve/<int:min_run_id>/<int:max_run_id>/",
        views.ConfigurationsForRunMinMaxView.as_view(),
        name="conf_for_run_min_max",
    ),
    path(
        "retrieve/<str:name>/<int:run_id>/",
        views.ConfigurationRetrieveView.as_view(),
        name="params_for_class",
    ),
    path(
        "retrieve/validity/latest/<int:run_id>/",
        views.LatestConfigurationValidityDatesForRunView.as_view(),
        name="latest_validity_for_run",
    ),
    path(
        "retrieve/validity/latest/<int:min_run_id>/<int:max_run_id>",
        views.LatestConfigurationValidityDatesForRunMinMaxView.as_view(),
        name="latest_validity_for_run_min_max",
    ),
    path("runs/", views.FilesCreateView.as_view(), name="runs_create"),
    path("api-token-auth/", auth_views.obtain_auth_token),
]
