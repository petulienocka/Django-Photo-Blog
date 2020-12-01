from django.contrib import admin
from django.urls import path

from .views import (PostListAPIView)


urlpatterns = [
    path('', PostListAPIView.as_view(), name='files'),

]
