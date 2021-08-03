from django.urls import path
from .views import post_list

urlpatterns = [
    path('', post_list, name='blog'),  # 127.0.0.1:8000/blog/
    path('post', post_list)  # 127.0.0.1:8000/blog/post

]
