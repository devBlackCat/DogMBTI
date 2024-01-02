from django.contrib import admin
from .models import DogsMbti, DogDetails, UserInfo

# 모델을 관리자 페이지에 등록
admin.site.register(DogDetails)
admin.site.register(DogsMbti)
admin.site.register(UserInfo)
