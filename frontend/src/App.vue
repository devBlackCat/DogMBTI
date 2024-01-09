<template>
   <img className="slide_image" :src="currentImage" alt="슬라이드 이미지" />
  <HelloWorld msg="Welcome to Your Vue.js App"/>
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
      images: [
        require('./assets/1.jpg'),
        require('./assets/2.jpg'),
        require('./assets/3.jpg'),
        require('./assets/4.jpg'),
        require('./assets/5.jpg'),
        require('./assets/6.jpg'),
      ],
      currentImageIndex: 0,
    }
  },
  computed: {
    currentImage() {
      return this.images[this.currentImageIndex];
    }
  },
  created() {
    setInterval(() => {
      this.currentImageIndex = (this.currentImageIndex + 1) % this.images.length;
    }, 3000); // 3초마다 이미지 변경
  },
 
  
}
</script>

<style>
.slide_image{
  width: 400px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
