from django.test import TestCase
from .models import FAQ
from .serializers import FAQSerializer

class FAQTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question="What is caching?", answer="Caching improves performance by storing temporary data.")

    def test_translation(self):
        # Test translation
        lang = 'hi'
        translated_question = translate_text(self.faq.question, lang)
        self.assertEqual(translated_question, "कैशिंग क्या है?")

    def test_cache(self):
        # Test caching
        cache.set("test_key", "cached_value", timeout=60)
        self.assertEqual(cache.get("test_key"), "cached_value")