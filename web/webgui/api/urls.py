from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('retrieve/<int:run_id>', views.ConfigurationsView.as_view(), name='configurations')
]


