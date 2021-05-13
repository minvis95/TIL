<template>
  <div>
    <h2>New Component!</h2>
    <h2>{{ myMessage }}</h2>
    <input @keyup.enter="childInputChange" v-model="childInputData" type="text">
  </div>
</template>

<script>
export default {
  name: 'NewComponent',
  data: function () {
    return {
      childInputData: '',
    }
  },
  props: {
    myMessage: {
      type: String,
      required: true,
    },
  },
  methods: {
    childInputChange: function () {
      this.$emit('child-input-change', this.childInputData)
    }
  }
}
</script>

<style>

</style>
