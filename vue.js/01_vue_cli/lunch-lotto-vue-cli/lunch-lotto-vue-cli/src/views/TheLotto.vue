<template>
  <div>
    <h1>로또 번호 추천</h1>
    <button @click="getLuckyNums">Pick My Lotto Numbers</button>
    <p>오늘의 추천 로또 번호</p>
    <!-- articles/1 에서 1같이 뒤에 붙은 숫자는 $route.params 들어있음 -->
    <p>로또 번호 {{ $route.params.lottoNum }}개 추천</p>
    <ul>
      <li v-for="(num, idx) in selectedLuckyNums" :key="idx">{{ num }}</li>
    </ul>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Thelotto',
  data: function () {
    return {
      selectedLuckyNums: [],
      sampleNums: 0,
    }
  },
  methods: {
    getLuckyNums: function () {
      const numbers = _.range(1, 46)
      this.sampleNums = _.sampleSize(numbers, this.$route.params.lottoNum)
      this.selectedLuckyNums = _.sortBy(this.sampleNums)

    }
  }
}
</script>

<style>

</style>