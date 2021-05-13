import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: []
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      // console.log(state)
      state.todos.push(todoItem)
    },
    DELETE_TODO: function (state, todoItem) {
      // console.log(state)
      // 1. todoItem이 첫번째로 만나는 요소의 index를 가져옴
      const index = state.todos.indexOf(todoItem)
      // 2. 해당 인덱스 1개만 삭제하고 나머지 요소를 토대로 새로운 배열 생성
      state.todos.splice(index, 1)
    },
    UPDATE_TODO: function (state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          return { ...todo, completed: !todo.completed }
        }
        return todo
      })
    }
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      // context.commit('CREATE_TODO', todoItem)
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodo: function ({ commit }, todoItem) {
      commit('UPDATE_TODO', todoItem)
    },
  },
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === false
      }).length
    },
  },
  modules: {
  }
})
