<template>
<!-- 부모 태그는 1개만 존재해야한다. -->
  <div>
    <h1>This is New Component</h1>
    <h1>This is New Component</h1>
    <h3>{{ message }}</h3>
    <h1>{{ msg }}</h1> <!-- 동작안함 -->
  </div>
</template>

<script>
export default {
  name: 'NewComponent', // Vue 탭에 뜨는 이름을 의미함
  props: {
    message: String,
    msg: String,
  }
}
</script>

<style>

</style>