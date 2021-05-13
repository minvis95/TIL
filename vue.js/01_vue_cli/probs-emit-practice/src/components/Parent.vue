<template>
  <div>
    <h1>Parent</h1>
    <input type="text" @input="onInput" :value="parentData">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <Child 
      :app-data="appData"
      :parent-data="parentData"
      :child-data="childData"
      @child-input="onChildInput"
    />
  </div>
</template>

<script>
import Child from '@/components/Child.vue'

export default {
  name: 'Parent',
  components: {
    Child,
  },
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
      this.$emit('parent-input', event.target.value)
    },
    onChildInput: function (childInput) {
      this.$emit('child-input', childInput)
    }
  }
}
</script>

<style>

</style>
