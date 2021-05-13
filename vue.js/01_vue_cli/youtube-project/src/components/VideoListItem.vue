<template>
  <li @click="selectVideo" class="list-group-item">
    <img :src="youtubeImgSrc" alt="thumbnails">
    <!-- <span v-html="video.snippet.title"></span> -->
    {{ video.snippet.title | stringUnescape }}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
    }
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    youtubeImgSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  },
}
</script>

<style>
.list-group .list-group-item {
  display: flex;        /* 가로 배치 및 flex의 CSS 적용 */
  margin-bottom: 1rem;  /* item의 상하 여백 */
  cursor: pointer;      /* 마우스를 포인터로 변경 */
}

.list-group .list-group-item:hover {
  background: #eee;
}

.list-group .list-group-item img {
  height: fit-content;   /* 텍스트가 길어져도 이미지는 늘어나지 않게 설정 */
  margin-right: 0.5rem;  /* 이미지와 텍스트 사이의 여백 */
}
</style>
