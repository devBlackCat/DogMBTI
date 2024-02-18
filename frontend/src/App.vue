<template>
  <div id="app_body">
   <header class="app-header test-header">
        <a class="app-header-btn back" href="/"  title="뒤로가기">
          <img :src="backArrowImagePath" alt="뒤로가기" />
        </a>
        <a href="/" class="app-logo result-logo">
          <img :src="logoImagePath" alt="로고" />
        </a>
      </header>
   <HelloWorld :slideImages="images"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data() {
    return {
      backArrowImagePath: require('@/assets/back-arrow-b.png'),
        logoImagePath: require('@/assets/dogmbti.png'),
  
  
    }
  },

 
  
}
</script>

<style>
body{
  margin:0;
  padding:0;

}
#app{
  background-color:#f2f2f2;
}
#app_body{
  background-color: #fff;
  max-width: 800px;
  margin: 0 auto;
  border-radius: 10px;
  border-radius: 0.625rem; /* 10px */
    box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.1);
}
.app-header {
   
   padding: 10px 20px; /* 상하 좌우 여백 */
   display: flex; /* 플렉스박스 레이아웃 사용 */
   align-items: center; /* 세로 중앙 정렬 */
   justify-content: space-between; /* 요소들을 양 끝으로 정렬 */
 }


 .app-logo {
   color: #333; /* 로고 색상 */
   font-size: 20px; /* 로고 폰트 크기 */
   text-decoration: none; /* 링크 밑줄 제거 */
   max-width: 250px;
   margin: 0 auto;
 }
 .app-logo img {
   width: 100%;
 }

.slide_image{
  width: 400px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
 
}
</style>
