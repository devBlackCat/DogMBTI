import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dogmbti.settings')
django.setup()

# 이제 모델을 임포트할 수 있습니다.
from main.models import DogsMbti
import json

# JSON 파일이 있는 디렉토리
json_directory = 'json/'


# 디렉토리의 모든 JSON 파일을 순회
for filename in os.listdir(json_directory):
    if filename.endswith('.json'):
        file_path = os.path.join(json_directory, filename)

        # JSON 파일 열기 및 읽기
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # MBTI 유형 분해
            mbti_type = data['Dog MBTI']['Type']
            energy, mental, nature, tactics = mbti_type[:4]

            # 모델 인스턴스 생성 및 저장
            DogsMbti.objects.create(
                dog_name=data['name'],
                energy=energy,
                mental=mental,
                nature=nature,
                tactics=tactics
            )
