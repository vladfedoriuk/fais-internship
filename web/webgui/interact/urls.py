from django.urls import path
from . import views

app_name = 'interact'

urlpatterns = [
    path('add/', views.parse, name='parse'),
    path('retrieve/', views.extract, name='extract')
]