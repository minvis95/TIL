<template>
  <div class="search-bar">
    <input type="text" @keyup.enter="onInputKeyword">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInputKeyword: function (event) {
      // console.log(event.target.value)
      this.$emit('input-search', event.target.value)
    }
  }
}
</script>

<style>
.search-bar > input {
  width: 100%;
  padding: 0.5rem;
  font-size: 2rem;
}
</style>
