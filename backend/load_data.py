import os
import json
import django
from django.core import serializers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dogmbti.settings')
django.setup()

from main.models import DogDetails

def export_data():
    # DogDetails의 모든 객체를 조회
    dog_details = DogDetails.objects.all()

    # 조회된 객체들을 json 형식으로 변환
    data = serializers.serialize('json', dog_details)

    # 결과를 json 파일로 저장
    with open('D:/work/dogmbti/DogMBTI/dogmbti/dog_details_export.json', 'w', encoding='utf-8') as file:
        file.write(data)

    print("DogDetails 모델의 데이터가 성공적으로 json 파일로 저장되었습니다.")

if __name__ == '__main__':
    export_data()

'''
import os
import json
import django

# 장고 환경 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dogmbti.settings')
django.setup()

from main.models import DogDetails

def load_data():
    # json 파일들이 저장된 디렉토리 경로
    json_dir = 'D:/work/dogmbti/DogMBTI/dogmbti/json'
    
    # 모든 json 파일들을 순회
    for json_file_name in os.listdir(json_dir):
        # 파일 경로
        file_path = os.path.join(json_dir, json_file_name)
        
        # 파일을 열고 json 데이터를 로드
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            try:
                # DogDetails 객체를 생성하거나 업데이트합니다.
                dog_detail, created = DogDetails.objects.update_or_create(
                    id=data.get('id'),  # JSON 파일에서 id 값을 가져옵니다. 없으면 None을 반환합니다.
                    defaults={
                        'name': data['dog'],
                        'difficulty_level': data['difficulty_level'],
                        'difficulty_description': data['difficulty_description'],
                        'dog_mbti_type': data['dog_mbti_type'],
                        'dog_mbti_reason': data['dog_mbti_reason'],
                        'health_problems': data['health_problems'],
                        'characteristics': data['characteristics'],
                        'intelligence': data['intelligence'],
                        'opinion_content': data['opinion_content'],
                        'youtube_link': data.get('youtube_link', ' ')  # youtube_link가 없는 경우 공백을 기본값으로 사용합니다.
                    }
                )
                if created:
                    print(f'새로운 객체가 생성되었습니다: {dog_detail.name} ({dog_detail.dog_mbti_type})')
                else:
                    print(f'기존 객체가 업데이트되었습니다: {dog_detail.name} ({dog_detail.dog_mbti_type})')

            except Exception as e:
                print(f'오류 발생: {e}, 파일명: {json_file_name}')

if __name__ == '__main__':
    load_data()
'''