<template>
  <div>
    <h2>로또 번호 추첨</h2>
    <button @click="getLottoNums">로또 추첨!</button>
    <!-- <p>{{ $route.params }}</p> -->
    <p>{{ seletedLottoNums }}</p>

  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function () {
    return {
      sampleNums: [],
      seletedLottoNums: [],
    }
  },
  methods: {
    getLottoNums: function () {
      const numbers = _.range(1, 46)
      this.sampleNums = _.sampleSize(numbers, this.$route.params.lottoNum)
      this.seletedLottoNums = _.sortBy(this.sampleNums)
    }
  }
}
</script>

<style>

</style>
