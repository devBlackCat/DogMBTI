#main/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DogDetails, UserInfo
from .serializers import DogDetailsSerializer
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

class MBTIRecommendationView(APIView):
    def get(self, request, format=None):
        try:
            user_mbti = request.query_params.get('mbti')
            user_age = request.query_params.get('age')
            user_gender = request.query_params.get('gender')
            user_ip = self.get_client_ip(request)
            
            logger.info(f"받은 MBTI 유형: {user_mbti}, IP: {user_ip}")
            UserInfo.objects.create(ip=user_ip, mbti=user_mbti, age=user_age, gender=user_gender)

            if not user_mbti:
                logger.warning("MBTI 유형이 제공되지 않음")
                return Response({"error": "MBTI 유형이 제공되지 않았습니다."}, status=400)

            mbti_compatibility = {
            'infp':['enfj','entj'],
            'enfp':['infj','intj'],
            'infj':['enfp','entp'],
            'enfj':['infp','isfp'],
            'intj':['enfp','entp'],
            'entj':['infp','intp'],
            'intp':['entj','estj'],
            'entp':['enfp','intj'],
            'isfp':['enfj','esfj','estj'],
            'esfp':['isfj','istj'],
            'istp':['esfj','estj'],
            'estp':['isfj'],
            'isfj':['esfp','estp'],
            'esfj':['isfp','istp'],
            'istj':['esfp'],
            'estj':['intp','isfp','istp']
            }    

            compatible_mbtis = mbti_compatibility.get(user_mbti.lower(), [])
            if not compatible_mbtis:
                logger.warning(f"유효하지 않은 MBTI 유형: {user_mbti}")
                return Response({"error": "유효하지 않은 MBTI 유형입니다."}, status=400)

            # 첫 번째 MBTI 유형에 대한 정보 검색
            main_mbti_type = compatible_mbtis[0]
            main_details = DogDetails.objects.filter(dog_mbti_type=main_mbti_type.upper()).first()
            main_dog_data = DogDetailsSerializer(main_details).data if main_details else None

            # 나머지 MBTI 유형에 대한 정보 검색
            other_mbti_data = []
            for mbti in compatible_mbtis[1:]:
                other_details = DogDetails.objects.filter(dog_mbti_type=mbti.upper())
                for detail in other_details:
                    other_mbti_data.append(DogDetailsSerializer(detail).data)

            # 응답 데이터 구성
            response_data = {
                "details": main_dog_data,
                "otherMbti": other_mbti_data
            }

            return Response(response_data)

        except Exception as e:
            logger.error(f"서버 내부 오류: {str(e)}")
            return JsonResponse({"error": "서버 내부 오류가 발생했습니다."}, status=500)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip