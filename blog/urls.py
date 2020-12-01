from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.photo_files, name='photo_files'),
    path('create', views.photo_create, name='photo_create'),
    path('detail/<int:id>/', views.photo_detail, name='photo_detail'),
    path('detail/<int:id>/update', views.photo_update, name='photo_update'),
    path('detail/<int:id>/delete', views.photo_delete, name='photo_delete'),
]
