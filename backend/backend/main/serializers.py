# main/serializers.py

from rest_framework import serializers
from .models import DogDetails

class DogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogDetails
        fields = ['id', 'name', 'difficulty_level', 'difficulty_description', 'dog_mbti_type', 'dog_mbti_reason', 'health_problems', 'characteristics', 'intelligence', 'opinion_content', 'youtube_link']
