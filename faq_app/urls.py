from django.urls import path
from .views import FAQListCreateAPIView

urlpatterns = [
    path('', FAQListCreateAPIView.as_view(), name='faq-list'),
]