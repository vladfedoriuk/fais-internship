from django.urls import path
from . import views

app_name = 'interact'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('add/', views.ParseView.as_view(), name='parse'),
    path('retrieve/', views.ExtractView.as_view(), name='extract'),
    path('download/', views.download, name='download'),
    path('release/', views.ReleaseView.as_view(), name='release'),
    path('login/', views.InteractLoginView.as_view(), name='login')
]