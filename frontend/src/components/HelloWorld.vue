<template>
  <div>
    <h1>MBTI 견종 추천</h1>
    <input v-model="userMbti" placeholder="당신의 MBTI를 입력하세요" />
    <button @click="getMbtiRecommendation">추천 받기</button>

    <div v-if="loading">로딩 중...</div>

    <div v-if="recommendation">
      <h2>추천 견종:</h2>
      <ul>
        <li v-for="(dog, index) in recommendation" :key="index">
          {{ dog.dog_name }}
          <ul>
            <li v-for="detail in dog.details" :key="detail.id">
              {{ detail.difficulty_level }} - {{ detail.difficulty_description }}
            </li>
          </ul>
        </li>
      </ul>
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
    axios.get('http://localhost:8000/api/mbti/', { params: { mbti: this.userMbti } })
      .then(response => {
        this.recommendation = response.data.results;
        this.loading = false;
      })
      .catch(error => {
        console.error("Error fetching data:", error);
        console.log("Requested URL:", error.config.url); // 요청된 URL 로깅
        this.loading = false;
      });
  },
},

};
</script>

<style>
/* 스타일 작성 */
</style>
