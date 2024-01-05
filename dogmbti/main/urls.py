from django.urls import path
from .views import MBTIRecommendationView

urlpatterns = [
    path('', MBTIRecommendationView.as_view(), name='mbti-recommendation'),
]
