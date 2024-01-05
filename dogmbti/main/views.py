from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DogsMbti, DogDetails
from .serializers import DogsMbtiSerializer, DogDetailsSerializer
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

class MBTIRecommendationView(APIView):
    def get(self, request, format=None):
        try:
            user_mbti = request.query_params.get('mbti')
            logger.info(f"받은 MBTI 유형: {user_mbti}")  # 추가된 로깅
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

            results = []
            for mbti in compatible_mbtis:
                details = DogDetails.objects.filter(dog_mbti_type=mbti.upper())
                logger.info(f"견종 상세 정보 조회 결과: {details}")  # 로그 추가

                for detail in details:
                    dog = detail.dog
                    dog_data = {
                        "dog_name": dog.dog_name,
                        "details": DogDetailsSerializer(detail).data
                    }
                    results.append(dog_data)

            logger.info(f"서버 응답 데이터: {results}")  # 로그 추가
            return Response({"results": results})

        except Exception as e:
            logger.error(f"서버 내부 오류: {str(e)}")
            return JsonResponse({"error": "서버 내부 오류가 발생했습니다."}, status=500)
