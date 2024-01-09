<template>
  <div class="mbti-container">
    <h1>MBTI로 알아보는 추천하는 견종 테스트</h1>
    <p>MBTI를 선택하고, 나이와 성별을 입력하면 추천 견종을 알려드립니다.</p>

    <div class="input-group">
      <select v-model="userMbti">
        <option disabled value="">당신의 MBTI를 선택하세요</option>
        <option v-for="mbti in Object.keys(mbtiCompatibility)" :key="mbti" :value="mbti">
          {{ mbti.toUpperCase() }}
        </option>
      </select>
      <select v-model="userGender">
        <option disabled value="">성별 선택</option>
        <option value="M">남성</option>
        <option value="F">여성</option>
        <option value="O">기타</option>
      </select>
      <input type="number" v-model="userAge" placeholder="나이" />
    </div>

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
      userAge: '',
      userGender: '',
      recommendation: null,
      loading: false,
      mbtiCompatibility : {
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
    };
  },
  methods: {
    getMbtiRecommendation() {
      this.loading = true;
      axios.get('http://127.0.0.1:8000/api/mbti/', { params: { mbti: this.userMbti } })
        .then(response => {
          console.log("서버 응답:", response.data);
          if (response.data.results && response.data.results.length > 0) {
            this.recommendation = response.data.results[0];
            console.log("추천 데이터:", this.recommendation);
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
.mbti-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  color: #333;
  font-family: 'Arial', sans-serif;
}

.mbti-container h1 {
  text-align: center;
  margin-bottom: 10px;
  color: #4CAF50;
}

.mbti-container p {
  text-align: center;
  margin-bottom: 20px;
}

.input-group {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-direction: column;
  width: 100%;
  margin-bottom: 20px;
}

.input-group select, .input-group input[type="number"] {
  padding: 10px;
  border: 2px solid #4CAF50;
  border-radius: 5px;
  background-color: white;
  font-size: 16px;
  width: 80%;
  margin: 0 auto;
  height: 40px;
  box-sizing: border-box;
}

.input-group select:hover, .input-group input[type="number"]:hover {
  border-color: #45a049;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 15px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s, box-shadow 0.3s;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

button:hover {
  background-color: #45a049;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

@media (max-width: 600px) {
  .mbti-container {
    padding: 15px;
  }

  .mbti-container h1 {
    font-size: 20px;
  }

  .mbti-container p {
    font-size: 14px;
    padding: 0 10px;
  }

  .input-group select, .input-group input[type="number"] {
    width: 90%;
    font-size: 14px;
  }

  button {
    font-size: 14px;
    padding: 12px 15px;
    width: 90%;
    margin: 10px auto;
  }

  .input-group {
    gap: 15px;
  }
}
</style>
