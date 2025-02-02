from django.urls import path
from .views import FAQListCreateAPIView

urlpatterns = [
    path('faqs/', FAQListCreateAPIView.as_view(), name='faq-list'),

]