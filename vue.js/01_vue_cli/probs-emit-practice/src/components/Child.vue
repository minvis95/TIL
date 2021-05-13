<template>
  <div>
    <h2>Child</h2>
    <input type="text" @input="onInput" :value="childData">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  props: {
    appData: {
      type: String,
    },
    parentData: {
      type: String,
    },
    childData: {
      type: String,
    }
  },
  methods: {
    onInput: function (event) {
      this.$emit('child-input', event.target.value)
    }
  }
}
</script>

<style>

</style>
