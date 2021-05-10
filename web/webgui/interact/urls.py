from django.urls import path, re_path
from . import views
from django.urls import reverse_lazy

from django.views.generic.base import RedirectView

app_name = 'interact'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('add/', views.ParseView.as_view(), name='parse'),
    path('retrieve/', views.ExtractView.as_view(), name='extract'),
    path('download/', views.download, name='download'),
    path('release/', views.ReleaseView.as_view(), name='release'),
    path('login/', views.InteractLoginView.as_view(), name='login'),
    path('logout/', views.InteractLogoutView.as_view(), name='logout'),
    path('files/', views.FilesListView.as_view(), name='files'),
    re_path(r'^.*$', RedirectView.as_view(url=reverse_lazy('interact:main'))),
]