from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_translated_question(self, lang='en'):
        cache_key = f"faq_{self.id}_question_{lang}"
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation

        translation_field = f'question_{lang}'
        translated_text = getattr(self, translation_field, None)

        if not translated_text:
            try:
                translated_text = translator.translate(self.question, dest=lang).text
                setattr(self, translation_field, translated_text)
                self.save()
            except Exception as e:
                print(f"Translation failed: {e}")
                translated_text = self.question  # Fallback to English

        cache.set(cache_key, translated_text, timeout=86400)  # Cache for 1 day
        return translated_text