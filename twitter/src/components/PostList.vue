<template>
  <div class="posts">
    <post-item  v-for="post in posts" :post="post" :key="post.id"
                @addLike="$emit('addLike', post)"
                @addDislike="$emit('addDislike', post)"/>
  </div>
</template>

<script>
import PostItem from "@/components/PostItem";

export default {
  name: "PostList",
  components: {
    PostItem
  },
  props: {
    posts: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>

</style>