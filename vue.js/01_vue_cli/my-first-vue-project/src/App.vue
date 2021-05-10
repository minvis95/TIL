<template>
  <div id="app">
    <a>이 태그의 글자색은...?</a>
    <img alt="Vue logo" src="./assets/logo.png">
    <NewComponent message="app에서 New컴포넌트로 보내는 거" msg="ㅋㅋㅋㅋ"/> <!-- 3. 컴포넌트 사용 / 주의  -->
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <HelloWorld msg="광주 2반에 오신 것을 환영해.."/>
  </div>
</template>

<script>
// 컴포넌트 사용하는 방법
// 1. 컴포넌트를 불러온다.
import HelloWorld from './components/HelloWorld.vue'
import NewComponent from './components/NewComponent.vue'

export default {
  name: 'App',
  components: {
    // 2. 컴포넌트를 등록한다.
    HelloWorld,
    NewComponent,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
