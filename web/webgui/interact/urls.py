from django.urls import path
from . import views

app_name = 'interact'

urlpatterns = [
    path('add/', views.ParseView.as_view(), name='parse'),
    path('retrieve/', views.ExtractView.as_view(), name='extract'),
    path('download/', views.download, name='download'),
    path('release/', views.ReleaseView.as_view(), name='release')
]