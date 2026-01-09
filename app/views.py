# views.py - Yangilangan
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *


class YangiliklarViewSet(viewsets.ModelViewSet):
    queryset = Yangiliklar.objects.all().order_by('-created_at')
    serializer_class = YangiliklarSerializer
    
    def get_serializer_context(self):
        # Request context ni serializer ga berish
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    



class VideoLavhalarViewSet(viewsets.ModelViewSet):
    queryset = VideoLavhalar.objects.all().order_by('-created_at')
    serializer_class = VideoLavhalarSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    @action(detail=True, methods=['post'])
    def increment_views(self, request, pk=None):
        """Video ko'rishlar sonini oshirish"""
        video = self.get_object()
        video.views_count += 1
        video.save()
        return Response({'views_count': video.views_count})
    
    @action(detail=True, methods=['post'])
    def increment_likes(self, request, pk=None):
        """Video layklar sonini oshirish"""
        video = self.get_object()
        video.likes_count += 1
        video.save()
        return Response({'likes_count': video.likes_count})