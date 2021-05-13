<template>
  <ul class="video-list list-group">
    <VideoListItem 
      v-for="(video, idx) in videos" 
      :key="idx"
      :video="video"
      @select-video="onSelectVideo"
    />
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
    }
  },
  methods: {
    onSelectVideo: function (video) {
      // console.log(video)
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>
.video-list {
  /* 기본 margin, padding, 그리고 list-style 속성 초기화 */
  padding: 0;
  margin: 0;
  list-style-type: none;

  width: 30%; /* Detail, List의 7:3 가로비율 설정*/
}
</style>
