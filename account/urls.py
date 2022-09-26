from urllib.parse import urlparse
from django.urls import path


from . import views

urlpatterns = [
    path('register/', views.register_view, name='register-page'),
    path('login/', views.login_view, name='login-page'),

]
