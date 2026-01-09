# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'yangliklar', YangiliklarViewSet, basename='yangiliklar')
router.register(r'videolar', VideoLavhalarViewSet, basename='videolar')

urlpatterns = [
    path('', include(router.urls)),
]