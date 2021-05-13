<template>
  <div>
    <TodoListItem 
      v-for="(todo, idx) in todos" 
      :key="idx"
      :todo="todo"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    // todos: function () {
    //   return this.$store.state.todos
    // }
    ...mapState([
      'todos',
    ])
  }
}
</script>

<style>

</style>
