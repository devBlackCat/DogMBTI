# DB에 업데이트시 사용 python update_db.py
import os
import django

# 장고 설정 파일 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dogmbti.settings')
django.setup()

from main.models import DogsMbti, DogDetails

def update_dogdetails_name():
    # DogDetails의 모든 객체를 순회
    for dog_detail in DogDetails.objects.all():
        # DogDetails의 dog 필드를 사용하여 DogsMbti의 dog_name을 조회
        dog_mbti = DogsMbti.objects.get(id=dog_detail.dog_id)
        
        # DogDetails의 name 필드를 dog_name으로 업데이트
        dog_detail.name = dog_mbti.dog_name
        dog_detail.save()
        print(f'Updated DogDetails id {dog_detail.id}: name set to {dog_detail.name}')

if __name__ == '__main__':
    update_dogdetails_name()
