# app/admin.py
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

@admin.register(Yangiliklar)
class YangiliklarAdmin(TranslationAdmin):
    list_display = ('yangilik_nomi', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('yangilik_nomi', 'yangilik_nomi_ru', 'yangilik_nomi_en', 'yangilik_xaqida')

@admin.register(VideoLavhalar)
class VideoLavhalarAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'youtube_id', 'views_count', 'likes_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title_uz', 'title_ru', 'title_en', 'description_uz', 'youtube_id')
    readonly_fields = ('views_count', 'likes_count', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('youtube_id', 'thumbnail', 'duration')
        }),
        ("O'zbekcha", {
            'fields': ('title_uz', 'description_uz')
        }),
        ('Ruscha', {
            'fields': ('title_ru', 'description_ru')
        }),
        ('Inglizcha', {
            'fields': ('title_en', 'description_en')
        }),
        ('Statistika', {
            'fields': ('views_count', 'likes_count')
        }),
    )