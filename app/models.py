# models.py - vaqtinchalik
from django.db import models
from django.utils import timezone

class Yangiliklar(models.Model):
    yangilik_rasmi = models.ImageField(upload_to='yangiliklar/')
    yangilik_nomi = models.CharField(max_length=500)
    yangilik_xaqida = models.TextField()
    
    # Avval default qiymat bilan qo'shamiz
    created_at = models.DateTimeField(default=timezone.now)  # auto_now_add=True emas
    updated_at = models.DateTimeField(auto_now=True)  # Bu xato bermaydi

    def __str__(self):
        return self.yangilik_nomi
    

class VideoLavhalar(models.Model):
    # 3 tilda maydonlar
    title_uz = models.CharField(max_length=500, verbose_name="Video nomi (O'zbekcha)")
    title_ru = models.CharField(max_length=500, verbose_name="Video nomi (Ruscha)", blank=True)
    title_en = models.CharField(max_length=500, verbose_name="Video nomi (Inglizcha)", blank=True)
    
    description_uz = models.TextField(verbose_name="Video tavsifi (O'zbekcha)", blank=True)
    description_ru = models.TextField(verbose_name="Video tavsifi (Ruscha)", blank=True)
    description_en = models.TextField(verbose_name="Video tavsifi (Inglizcha)", blank=True)
    
    youtube_id = models.CharField(max_length=100, verbose_name="YouTube Video ID")
    thumbnail = models.ImageField(upload_to='video_thumbnails/', verbose_name="Video rasmi", blank=True, null=True)
    
    duration = models.CharField(max_length=20, verbose_name="Video davomiyligi", blank=True)
    views_count = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    likes_count = models.IntegerField(default=0, verbose_name="Layklar soni")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Video Lavhalar"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title_uz
    
    # Tilga qarab ma'lumot olish funksiyasi
    def get_title(self, lang='uz'):
        if lang == 'ru' and self.title_ru:
            return self.title_ru
        elif lang == 'en' and self.title_en:
            return self.title_en
        return self.title_uz
    
    def get_description(self, lang='uz'):
        if lang == 'ru' and self.description_ru:
            return self.description_ru
        elif lang == 'en' and self.description_en:
            return self.description_en
        return self.description_uz or ""