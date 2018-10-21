"""
Omoads URL Configuration
"""
from django.contrib import admin
from django.urls import path
from banners import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
]
