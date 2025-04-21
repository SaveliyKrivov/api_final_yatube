from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
