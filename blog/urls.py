from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blog_posts/', views.blog_posts, name='blog_posts'),
    # path('post_list', views.post_list, name='post_list'),
    path('single_posts', views.single_posts, name='single_posts'),
]