import os
import django

# Django 환경 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dogmbti.settings')
django.setup()

# 이제 모델을 임포트할 수 있습니다.
from main.models import DogsMbti, DogDetails
import json

# JSON 파일 디렉토리
json_directory = 'json/'

# JSON 파일을 순회하며 데이터 처리
for filename in os.listdir(json_directory):
    if filename.endswith('.json'):
        file_path = os.path.join(json_directory, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # DogsMbti 모델에서 해당하는 dog_name을 찾음
            dog_instance = DogsMbti.objects.filter(dog_name=data['name']).first()

            if dog_instance:
                DogDetails.objects.create(
                    dog=dog_instance,
                    difficulty_level=data['Difficulty Level']['Rating'],
                    difficulty_description=data['Difficulty Level']['Description'],
                    dog_mbti_type=data['Dog MBTI']['Type'],
                    dog_mbti_reason=data['Dog MBTI']['Reason'],
                    health_problems=data['Detailed Information']['Problems'],
                    characteristics=data['Detailed Information']['Characteristics'],
                    intelligence=data['Detailed Information']['Intelligence'],
                    opinion_content=data['Opinion']['Content']
                )
