<template>
  <div>
    <h2>점심메뉴 추천</h2>
    <button @click="pickOneLunchMenu">메뉴추천!</button>
    <p>오늘의 점심 메뉴 : {{ selectedLunchMenu }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch: ['간장계란밥', '스팸', '시래기국밥'],
      selectedLunchMenu: '',
    }
  },
  methods: {
    pickOneLunchMenu: function () {
      this.selectedLunchMenu = _.sample(this.lunch)
    }
  }
}
</script>

<style>

</style>
