from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

app_name = "api"

urlpatterns = [
    path(
        "retrieve/<int:run_id>",
        views.ConfigurationsView.as_view(),
        name="configurations",
    ),
    path("api-token-auth/", auth_views.obtain_auth_token),
]
