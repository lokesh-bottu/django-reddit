# core/urls.py

from django.urls import path
from .views import success_page, create_post_view

app_name = 'user'
urlpatterns = [
    path('success/', success_page, name='success_page'),
    path('create_post/', create_post_view, name='create_post'),
]
