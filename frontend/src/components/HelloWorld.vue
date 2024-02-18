<template>
  <div class="mbti-container">
    <img v-if="!recommendationData" className="main_image" :src="mainImage" alt="슬라이드 이미지" />
    <!-- 추천 견종이 있을 경우만 DogRecommendation 컴포넌트 표시 -->
    <DogRecommendation v-if="recommendationData" :recommendationData="recommendationData"/>

    <!-- 추천 견종이 없을 경우 입력 양식 표시 -->
    <div v-if="!recommendationData">
      <h1>MBTI로 알아보는 추천하는 견종 테스트</h1>
      <p>MBTI를 선택하시면 MBTI 궁합표를 참고해서 가장 잘 맞는 MBTI의 견종을 추천해드립니다.</p>
    
    
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
        <button @click="getMbtiRecommendation">추천 받기</button>
      </div>


      <div v-if="loading">로딩 중...</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import DogRecommendation from './DogRecommendation.vue';

export default {
  components: {
    DogRecommendation,
  },

  data() {
    return {
      mainImage: require('@/assets/main.jpg'),
      userMbti: '',
      userAge: '',
      userGender: '',
      recommendationData: null,
      loading: false,

      currentImageIndex: 0,
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
    // 필수 필드가 비어 있거나 나이가 숫자가 아닌 경우 경고
    if (!this.userMbti || !this.userAge || isNaN(this.userAge) || !this.userGender) {
      alert("모든 필드를 정확히 채워주세요.");
      return;
    }

    this.loading = true;
    axios.get('http://dogmbti.site/api/mbti/', { params: { mbti: this.userMbti, age: this.userAge, gender: this.userGender } })
      .then(response => {
        console.log("서버 응답:", response.data);

        if (response.data.details) {
          this.recommendationData  = response.data
          console.log("추천 데이터:", this.recommendationData );
        } else {
          this.recommendationData = null;
        }
        this.loading = false;
      })
      .catch(error => {
        console.error("Error fetching data:", error);
        this.loading = false;
      });
  },
}
,


};
</script>


<style>
ul,li{
  list-style: none;
}

.main_image{
  width: 100%;
  max-width:450px;
  margin: 0 auto;
}
.mbti-container {
 
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
  font-size: 1rem; /* 수정됨: 16px -> 1rem */
  width: 80%;
  margin: 0 auto;
  height: 40px;
  box-sizing: border-box;
  color: #000;
}
.input-group input[type="number"]::placeholder {
  color: #000;
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
  font-size: 1rem; /* 수정됨: 16px -> 1rem */
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
    font-size: 1.25rem; /* 수정됨: 20px -> 1.25rem */
  }

  .mbti-container p {
    font-size: 0.875rem; /* 수정됨: 14px -> 0.875rem */
    padding: 0 10px;
  }

  .input-group select, .input-group input[type="number"] {
    width: 90%;
    font-size: 0.875rem; /* 수정됨: 14px -> 0.875rem */
  }

  button {
    font-size: 0.875rem; /* 수정됨: 14px -> 0.875rem */
    padding: 12px 15px;
    width: 90%;
    margin: 10px auto;
  }

  .input-group {
    gap: 15px;
  }
}
html {
    font-size: 16px; /* 기본 폰트 크기 */
  }

  /* 화면 너비가 600px 이하일 때 */
  @media screen and (max-width: 600px) {
    html {
      font-size: 15px;
    }
  }

  /* 화면 너비가 500px 이하일 때 */
  @media screen and (max-width: 500px) {
    html {
      font-size: 14px;
    }
  }

  /* 화면 너비가 400px 이하일 때 */
  @media screen and (max-width: 400px) {
    html {
      font-size: 14.5px;
    }
  }

  /* 화면 너비가 300px 이하일 때 */
  @media screen and (max-width: 300px) {
    html {
      font-size: 13px;
    }
  }
</style>
