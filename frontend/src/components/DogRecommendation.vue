<template>
  <div v-if="localRecommendationData" class="recommendation-container">
    <h2>추천 견종: {{ localRecommendationData.dog_name }}</h2>
    <div class="detail-section">
      <div class="dog-mbti-type">{{ localRecommendationData.details.dog_mbti_type }}</div>
      <img v-if="getImagePath(localRecommendationData.details.id)" class="dog-image" :src="getImagePath(localRecommendationData.details.id)" alt="견종 이미지" />
      <div class="dog-mbti-reason">{{ localRecommendationData.details.dog_mbti_reason }}</div>
      <div class="difficulty-level">{{ convertToStars(localRecommendationData.details.difficulty_level) }}</div>
      <ul class="info-list">
        <li><strong>난이도 설명:</strong> {{ localRecommendationData.details.difficulty_description }}</li>
        <li><strong>건강 문제:</strong> {{ localRecommendationData.details.health_problems }}</li>
        <li><strong>지능:</strong> {{ localRecommendationData.details.intelligence }}</li>
        <li><strong>의견:</strong> {{ localRecommendationData.details.opinion_content }}</li>
      </ul>
      <p class="other-dogs-title">그외 추천할 견종</p>
      <ul v-if="localRecommendationData.otherMbti && localRecommendationData.otherMbti.length" class="other-dogs-list">
        <li v-for="dog in localRecommendationData.otherMbti.slice(0, 3)" :key="dog.id" class="other-dog-item" @click="swapDetails(dog)">
          <p class="other-dog-name">{{ dog.name }}</p>
          <div class="other-dog-image">
            <!--<img v-if="getImagePath(dog.id)" :src="getImagePath(dog.id)" alt="견종 이미지" />-->
            <div v-if="getImagePath(dog.id)" :style="{ backgroundImage: 'url(' + getImagePath(dog.id) + ')' }" class="dog-image02" alt="견종 이미지">  </div>
          </div>  
        </li>
      </ul>
      <p v-else class="no-additional-dogs">추가적인 견종이 없습니다.</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    recommendationData: Object
  },
  data() {
    return {
      // 로컬 데이터를 초기화하고 prop의 내용을 복사합니다.
      localRecommendationData: JSON.parse(JSON.stringify(this.recommendationData))
    };
  },
  created() {
    this.shuffleOtherMbti();
  },
  mounted() {
    console.log(this.recommendationData);
  },
  methods: {
    shuffleOtherMbti() {
      if (this.localRecommendationData.otherMbti.length > 3) {
        for (let i = this.localRecommendationData.otherMbti.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [this.localRecommendationData.otherMbti[i], this.localRecommendationData.otherMbti[j]] = [this.localRecommendationData.otherMbti[j], this.localRecommendationData.otherMbti[i]];
        }
      }
    },
    swapDetails(selectedDog) {
      // 로컬 데이터를 업데이트
      let currentDetails = this.localRecommendationData.details;
      this.localRecommendationData.details = selectedDog;
      this.localRecommendationData.otherMbti = this.localRecommendationData.otherMbti.filter(dog => dog.id !== selectedDog.id);
      this.localRecommendationData.otherMbti.push(currentDetails);

      // 변경된 내용을 이벤트를 통해 부모 컴포넌트에 전달
      this.$emit('update-recommendation-data', this.localRecommendationData);
    },
    convertToStars(difficulty) {
      const [score, total] = difficulty.split('/').map(Number);
      const maxStars = 5;
      const normalizedScore = (score / total) * maxStars;
      const fullStars = '★'.repeat(Math.floor(normalizedScore));
      const halfStar = (normalizedScore % 1 >= 0.5) ? '★' : '';
      const emptyStars = '☆'.repeat(maxStars - Math.floor(normalizedScore) - (halfStar ? 1 : 0));
      return fullStars + halfStar + emptyStars;
    },
    getImagePath(id) {
      const formattedId = id < 10 ? '0' + id : id;
      try {
        return require(`@/assets/dog/${formattedId}.jpg`);
      } catch (error) {
        // 이미지를 찾을 수 없을 때 기본 이미지 경로를 반환합니다.
        // 'default.jpg'를 해당 경로에 적절한 기본 이미지 파일명으로 바꿔주세요.
        return '@/assets/dog/default.jpg';
      }
    }
  }
};
</script>


<style>
.recommendation-container {
  padding: 1.25rem; /* 20px */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 아이디어 1: 그림자 추가 */
  background-color: #f8f8f8;
}

.recommendation-container .dog-image {
  width: 100%;
  border-radius: 2rem;
  margin-bottom: 0.625rem; /* 10px */
  transition: transform 0.3s; /* 아이디어 2: 호버 효과 */
}

.recommendation-container .dog-image:hover {
  transform: scale(1.05); /* 아이디어 2: 호버 효과 */
}

.recommendation-container h2 {
  color: #4CAF50;
  margin-bottom: 0.9375rem; /* 15px */
  position: relative; /* 아이디어 3: 아이콘 추가를 위한 설정 */
}



.detail-section {
  text-align: left;
}

.detail-section > div strong {
  color: #333;
  font-weight: bold;
}

.dog-mbti-type, .dog-mbti-reason, .difficulty-level {
  text-align: center;
  margin: 0.625rem; /* 10px */
}

.dog-mbti-type {
  font-size: 2rem; /* 32px -> 2rem */
}

.dog-mbti-reason {
  font-size: 1.125rem; /* 18px -> 1.125rem */
  width: 90%;
  margin: 0 auto;
  white-space: pre-wrap;
}

.difficulty-level {
  font-size: 4rem; /* 64px -> 4rem */
  line-height: 1; /* 기본값보다 작게 설정 */
  text-align: center;
  margin: 2rem 0; /* 필요에 따라 조정 */
  color: #ff5252; /* 별점 색상 레드 계열로 변경 */
}

.info-list {
  list-style-type: none; /* 기본 리스트 스타일 제거 */
  background-color: #fff; /* 배경 색상 */
  border: 1px solid #ddd; /* 테두리 */
  padding: 15px; /* 내부 여백 */
  border-radius: 10px; /* 테두리 둥글게 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 아이디어 1: 그림자 추가 */
}

.info-list li {
  padding: 10px 0; /* 항목 상하 여백 */
  border-bottom: 1px solid #ddd; /* 항목 사이의 구분선 */
  transition: background-color 0.3s; /* 아이디어 2: 호버 효과 */
}

.info-list li:hover {
  background-color: #e8e8e8; /* 아이디어 2: 호버 효과 */
}

.info-list li:last-child {
  border-bottom: none; /* 마지막 항목의 하단선 제거 */
}
.other-dogs-title {
  font-size: 1.25rem; /* 20px -> 1.25rem */
  color: #4CAF50;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
}

.other-dogs-list {
  list-style-type: disc; /* 항목 앞에 디스크 스타일 */
  padding-left: 20px; /* 내부 여백 */
}
.no-additional-dogs {
  color: #666;
  font-style: italic;
}

/* .other-dogs-list에 대한 스타일 추가 */
.other-dogs-list {
 
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0,0,0,.1);
  margin-bottom: 10px;
  overflow-x: auto; /* 가로 스크롤 허용 */
  white-space: nowrap; /* 요소들을 한 줄로 표시 */
  display: block; /* 블록 레벨 요소로 설정 */
}

/* .other-dog-item에 대한 스타일 수정 */
.other-dog-item {
  display: inline-block; /* 요소를 인라인 블록으로 설정 */
  vertical-align: top; /* 요소를 상단 정렬 */
  margin-right: 10px; /* 오른쪽 여백 */
  transition: transform .3s ease-in-out;
  width: 31.9%;
  border: 1px solid #ddd;
  border-radius: 20px;
  cursor: pointer; /* 손가락 모양으로 변경 */
  transition: transform .3s ease-in-out, box-shadow .3s ease-in-out; /* 호버 효과를 위한 트랜지션 */
  box-shadow: 0 2px 4px rgba(0,0,0,.1); /* 그림자 효과 */
  background-color: #fff;
  overflow: hidden; /* 요소의 내용이 너무 길어지면 숨김 */
 
}
.other-dog-item:hover {
  transform: translateY(-3px); /* 호버 시 약간 위로 이동 */
  box-shadow: 0 4px 8px rgba(0,0,0,.1); /* 호버 시 그림자 효과 강화 */
}
/* 마지막 .other-dog-item의 마진 제거 */
.other-dog-item:last-child {
  margin-right: 0;
}

.other-dog-name {
  font-size: 1rem; /* 글자 크기 */
  color: #333; /* 글자 색상 */
  margin-bottom: 5px; /* 아래쪽 여백 */
  text-align: center; /* 텍스트 중앙 정렬 */
}

.other-dog-image p {
  text-align: center; /* 이미지 중앙 정렬 */
}

.other-dog-image img {
  width: auto; /* 이미지 너비 자동 조정 */
  max-width: 100%; /* 최대 너비 */
  height: auto; /* 높이 자동 조정 */
  display: block; /* 블록 레벨 요소로 표시 */

}

.dog-image02{
  width: 100%; /* 이미지의 너비 */
  height: 150px; /* 이미지의 높이 */
  background-size: cover; /* 이미지가 컨테이너를 가득 채우도록 */
  background-position: center; /* 이미지를 중앙에 위치 */

  /* 필요에 따라 추가 스타일링 */
}


/* 500px 이하 적용되는 스타일 */
@media screen and (max-width: 600px) {
  .difficulty-level {
    font-size: 3rem; /* 48px -> 3rem */
  }
  #app .other-dogs-list{
    display: flex; 
    flex-direction: column;    

    box-shadow:none;
  }
  .dog-image02 {  height: 260px;}
  .other-dog-item {    width: 100%;    margin-bottom: 3rem;}
}
@media screen and (max-width: 400px) {
  .dog-image02 {  height: 240px;}
}
</style>
