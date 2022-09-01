<template>
  <div class="post">
    <h2 class="post-title">{{ post.title }}</h2>
    <p class="post-body">{{ post.body }}</p>
    <div @click="$emit('addLike', post)"> <strong>{{ post.likes }}</strong> ❤️ </div>
    <div @click="$emit('addDislike', post)"> <strong>{{ post.dislikes }}</strong> 👎 </div>
  </div>
</template>

<script>
export default {
  name: "PostItem",
  props: {
    post: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.post{
  width: 680px;
  height: auto;
  margin-top: 15px;
  border: 1px solid teal;
}
</style>