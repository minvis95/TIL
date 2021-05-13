<template>
  <div>
    <!-- 첫번째는 클릭해도 동작하지 않음 -->
    <HelloWorld @click="onClick"/> 
    <HelloWorld @click.native="onClick"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
    HelloWorld
  },
  methods: {
    onClick: function () {
      console.log('hello')
    }
  }
}
</script>

<style>

</style>
