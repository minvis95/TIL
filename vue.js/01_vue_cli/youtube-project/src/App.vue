<template>
  <div id="app">
    <h1>My first youtube project</h1>
    <header>
      <SearchBar @input-search="onInputSearch"/>
    </header>
    <section>
      <VideoDetail :video="selectVideo"/>
      <VideoList 
        :videos="videos"
        @select-video="onVideoSelect"
      />
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from '@/components/VideoDetail.vue'


const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'


export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      searchData: '',
      videos: [],
      selectVideo: '',
    }
  },
  methods: {
    onVideoSelect: function (video) {
      // console.log(video)
      this.selectVideo = video
    },
    onInputSearch: function (searchData) {
      // console.log('searchbar의 이벤트가 감지되었다!')
      // console.log(searchData)
      this.searchData = searchData

      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.searchData,
      }

      axios({
        url: API_URL,
        method: 'get',
        params,
      })
        .then(res => {
          // console.log(res)
          console.log(res.data.items)
          this.videos = res.data.items
          this.selectVideo = this.videos[0]
        })
        .catch(err => {
          console.log(err)
        })
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

section,
header {
  width: 80%;
  margin: 0 auto;
  padding: 1rem 0;
}

section {
  display: flex;
}
</style>
