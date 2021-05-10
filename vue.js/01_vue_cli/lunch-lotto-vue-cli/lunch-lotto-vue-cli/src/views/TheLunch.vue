<template>
  <div>
    <h2>점심 메뉴 추천</h2>
    <h1>{{ lunch }}</h1>
    <button @click="pickOneInLunchMenu">점심 메뉴 추천 해주세요!</button>
    <p>오늘의 추천 메뉴는: {{ selectedLunchMenu }}</p>
    <input type="text" v-model="lottoNum" placeholder="추천 받고 싶은 번호 갯수를 입력">
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch: ['국밥', '짜장면', '햄버거'], // 0, 1, 2
      selectedLunchMenu: '',
      lottoNum: 0,
    }
  },
  methods: {
    pickOneInLunchMenu: function () {
      const randomIndex = _.random(this.lunch.length - 1) 
      // -1을 하는 이유는 lodash의 random이 random(3)이면 0,1,2,3이 나와서
      this.selectedLunchMenu = this.lunch[randomIndex]
      // push redirect 같은거 다른 경로로 이동할 때 사용
      // push는 router-link를 클릭하는 것과 동일한 효과
      // push 할때 parameter 함께 보내기
      this.$router.push({ name: 'TheLotto', params: { lottoNum: this.lottoNum}})
    }
  }
}
</script>

<style>

</style>