# main/serializers.py

from rest_framework import serializers
from .models import DogsMbti, DogDetails

class DogsMbtiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogsMbti
        fields = ['id', 'dog_name', 'energy', 'mental', 'nature', 'tactics']

class DogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogDetails
        fields = ['id', 'dog_id', 'difficulty_level', 'difficulty_description', 'dog_mbti_type', 'dog_mbti_reason', 'health_problems', 'characteristics', 'intelligence', 'opinion_content', 'youtube_link']
