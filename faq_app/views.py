from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer
from rest_framework import serializers
from .utils import translate_text
from django.core.cache import cache

class FAQListCreateAPIView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.GET.get('lang', 'en')
        queryset = super().get_queryset()

        # Apply translations dynamically
        for faq in queryset:
            faq.question = faq.get_translated_question(lang)
        
        return queryset

    def _apply_pagination(self, queryset):
        page_size = 10
        page = self.request.GET.get('page')
        if page:
            start = (int(page) - 1) * page_size
            end = start + page_size
            return queryset[start:end]
        return queryset

    def _apply_filtering(self, queryset):
        filter_param = self.request.GET.get('filter')
        if filter_param:
            return queryset.filter(question__icontains=filter_param)
        return queryset

    def _apply_sorting(self, queryset):
        sort_param = self.request.GET.get('sort')
        if sort_param:
            return queryset.order_by(sort_param)
        return queryset