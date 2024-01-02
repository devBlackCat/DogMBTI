from django.db import models

# Create your models here.

class DogsMbti(models.Model):
    dog_name = models.CharField(max_length=100)
    energy = models.CharField(max_length=1, choices=[('E', 'Energetic'), ('I', 'Introverted')])
    mental = models.CharField(max_length=1, choices=[('N', 'Intuitive'), ('S', 'Sensing')])
    nature = models.CharField(max_length=1, choices=[('F', 'Feeling'), ('T', 'Thinking')])
    tactics = models.CharField(max_length=1, choices=[('J', 'Judging'), ('P', 'Perceiving')])

class DogDetails(models.Model):
    dog = models.ForeignKey(DogsMbti, on_delete=models.CASCADE)
    difficulty_level = models.CharField(max_length=3)
    difficulty_description = models.TextField()
    dog_mbti_type = models.CharField(max_length=4)
    dog_mbti_reason = models.TextField()
    health_problems = models.TextField()
    characteristics = models.TextField()
    intelligence = models.TextField()
    opinion_content = models.TextField()
    youtube_link = models.URLField()

class UserInfo(models.Model):
    ip = models.GenericIPAddressField()
    mbti = models.CharField(max_length=4)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
