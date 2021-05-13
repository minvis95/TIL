<template>
  <div id="app">
    <h2>App</h2>
    <input type="text" v-model="appData">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <Parent 
      :app-data="appData"
      :parent-data="parentData"
      :child-data="childData"
      @parent-input="onParentInput"
      @child-input="onChildInput"
    />
  </div>
</template>

<script>
import Parent from '@/components/Parent.vue'

export default {
  name: 'App',
  components: {
    Parent,
  },
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    onParentInput: function (parentData) {
      this.parentData = parentData
    },
    onChildInput: function (childData) {
      this.childData = childData
    }
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
