<template>
  <div id="app">
    <div id="nav">
      <router-link :to="{ name: 'TheLunch' }">Lunch</router-link> |
      <!-- <router-link to="/lotto">Lotto</router-link> -->
      <router-link :to="{ name: 'TheLotto' }">Lotto</router-link> |
      <!-- vue router로 파라미터 전달하기 -->
      <router-link :to="{ name: 'TheLotto', params: {lottoNum: 3} }">Lotto3</router-link> 
    </div>
    <router-view/> <!-- django의 {% block %} 같은거  -->
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
