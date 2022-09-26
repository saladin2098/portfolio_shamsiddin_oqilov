from django.urls import path

# my views
from . import views

urlpatterns = [
    path('', views.blog_view, name='blog-page'),
    path('inside_the_post/<int:pk>/', views.inside_the_post, name='inside-post'),
    path('like/<int:pk>/', views.save_like, name='save-like'),
    path('unlike/<int:pk>/', views.unlike, name='unlike'),
    path('dislike/<int:pk>/', views.dislike, name='dislike'),
    path('undislike/<int:pk>/', views.undislike, name='undislike'),

    path('save_comment/<int:post_id>', views.save_comment, name='save-comment'),
]
