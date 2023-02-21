from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('upload_file', views.upload_file, name='upload_file')
]