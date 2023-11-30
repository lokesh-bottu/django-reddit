from django.contrib import admin

# Register your models here.
# core/admin.py

from django.contrib import admin
from .models import UserProfile, Post, Comment

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
