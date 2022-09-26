from urllib.parse import urlparse
from django.urls import path


# my views
from . import views

urlpatterns = [
    path('', views.home1, name='home'),
    path('download_cv/<int:pk>', views.download_cv, name='download_cv'),
]
