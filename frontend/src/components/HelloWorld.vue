<template>
  <div>
    <h1>MBTI 견종 추천</h1>
    <input v-model="userMbti" placeholder="당신의 MBTI를 입력하세요" />
    <button @click="getMbtiRecommendation">추천 받기</button>

    <div v-if="loading">로딩 중...</div>

    <div v-if="recommendation">
      <h2>추천 견종:</h2>
      <div>
        {{ recommendation.dog_name }}
        <ul>
          <li v-for="detail in recommendation.details" :key="detail.id">
            {{ detail.difficulty_level }} - {{ detail.difficulty_description }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userMbti: '',
      recommendation: null,
      loading: false,
    };
  },
  methods: {
  getMbtiRecommendation() {
    this.loading = true;
    axios.get('http://127.0.0.1:8000/api/mbti/', { params: { mbti: this.userMbti } })

      .then(response => {
        console.log("서버 응답:", response.data); // 서버 응답 로그 출력
        if (response.data.results && response.data.results.length > 0) {
          this.recommendation = response.data.results[0];
          console.log("추천 데이터:", this.recommendation); // 추천 데이터 로그 출력
        } else {
          this.recommendation = null;
        }
        this.loading = false;
      })
      .catch(error => {
        console.error("Error fetching data:", error);
        this.loading = false;
      });
  },
},


};
</script>

<style>
/* 스타일 작성 */
</style>
