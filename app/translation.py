# app/translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import Yangiliklar, VideoLavhalar

class YangiliklarTranslationOptions(TranslationOptions):
    fields = ('yangilik_nomi', 'yangilik_xaqida')  # Bu yerda asl maydon nomlari

class VideoLavhalarTranslationOptions(TranslationOptions):
    # Modelda 'title' maydoni yo'q, shuning uchun modeldagi asl maydon nomlarini ishlatamiz
    fields = ('title_uz', 'description_uz')  # Asl maydon nomlarini ishlatamiz

translator.register(Yangiliklar, YangiliklarTranslationOptions)
translator.register(VideoLavhalar, VideoLavhalarTranslationOptions)
