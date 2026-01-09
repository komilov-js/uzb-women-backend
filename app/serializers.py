# serializers.py - Yangilangan
from rest_framework import serializers
from .models import *

class YangiliklarSerializer(serializers.ModelSerializer):
    # Yangilangan: request context qo'shildi
    class Meta:
        model = Yangiliklar
        fields = ['id', 'yangilik_rasmi', 'yangilik_nomi', 'yangilik_xaqida', 'created_at']
    
    def to_representation(self, instance):
        # Asosiy ma'lumotlarni olish
        data = super().to_representation(instance)
        
        # Request ni olish
        request = self.context.get('request')
        if request:
            # Til parametrini olish
            lang = request.GET.get('lang', 'uz')

            nama_field = f'yangilik_nomi_{lang}'
            if hasattr(instance, nama_field):
                translated_name = getattr(instance, nama_field)
                if translated_name and translated_name.strip():
                    data['yangilik_nomi'] = translated_name
            
            # Tarjimalangan matn
            xaqida_field = f'yangilik_xaqida_{lang}'
            if hasattr(instance, xaqida_field):
                translated_content = getattr(instance, xaqida_field)
                if translated_content and translated_content.strip():
                    data['yangilik_xaqida'] = translated_content
        
        # Rasmlar uchun to'liq URL
        if data.get('yangilik_rasmi') and not data['yangilik_rasmi'].startswith('http'):
            if request:
                data['yangilik_rasmi'] = request.build_absolute_uri(data['yangilik_rasmi'])
        
        return data
    
# app/serializers.py - VideoLavhalar uchun
class VideoLavhalarSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    youtube_url = serializers.SerializerMethodField()
    embed_url = serializers.SerializerMethodField()
    
    class Meta:
        model = VideoLavhalar
        fields = [
            'id', 'title', 'description', 'youtube_id', 
            'thumbnail', 'duration', 'views_count', 'likes_count',
            'created_at', 'updated_at', 'youtube_url', 'embed_url'
        ]
    
    def get_title(self, obj):
        request = self.context.get('request')
        lang = request.GET.get('lang', 'uz') if request else 'uz'
        return obj.get_title(lang)
    
    def get_description(self, obj):
        request = self.context.get('request')
        lang = request.GET.get('lang', 'uz') if request else 'uz'
        return obj.get_description(lang)
    
    def get_thumbnail(self, obj):
        if obj.thumbnail:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        return f'https://img.youtube.com/vi/{obj.youtube_id}/hqdefault.jpg'
    
    def get_youtube_url(self, obj):
        return f'https://www.youtube.com/watch?v={obj.youtube_id}'
    
    def get_embed_url(self, obj):
        return f'https://www.youtube.com/embed/{obj.youtube_id}'