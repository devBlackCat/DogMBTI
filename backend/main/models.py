from django.db import models

# Create your models here.

class DogDetails(models.Model):
    
    
    name = models.CharField(max_length=100, default='Default Name')  # Provide a default value for the 'name' field
    id = models.IntegerField(primary_key=True)
    difficulty_level = models.CharField(max_length=6)
    difficulty_description = models.TextField()
    dog_mbti_type = models.CharField(max_length=4)
    dog_mbti_reason = models.TextField()
    health_problems = models.TextField()
    characteristics = models.TextField()
    intelligence = models.TextField()
    opinion_content = models.TextField()
    youtube_link = models.TextField(default=' ')
    def __str__(self):
        # 리턴에 맨앞에 id를 붙여서 보내줌 
        return str(self.id)+'_ '+self.name+'('+self.dog_mbti_type+')'


class UserInfo(models.Model):
    ip = models.GenericIPAddressField()
    mbti = models.CharField(max_length=4)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    def __str__(self):
        return self.ip