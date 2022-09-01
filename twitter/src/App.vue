<template>
  <post-form @create="createPost"/>
  <post-list v-bind:posts="posts" @addLike="addLike" @addDislike="addDislike"/>
</template>

<script>
import PostForm from "@/components/PostForm";
import PostList from "@/components/PostList";
import axios from "axios";

export default {
  components: {
    PostForm,
    PostList
  },
  data(){
    return {
      posts: [
        {id: 1, title: '1984', body: 'Romane of George Orwell', likes: 1984, dislikes: 0},
        {id: 2, title: 'Hobbit', body: 'One of the greatest book in history', likes: 13450, dislikes: 0}
      ],
    }
  },
  beforeMount(){
    this.fetchPosts();
  },

  methods: {

    createPost(post) {
      this.posts.push(post)
    },

    addLike(post) {
      this.posts.forEach(element => {
        if (element.id == post.id) {
          element.likes++;
        }
      })
    },

    addDislike(post) {
      this.posts.forEach(element => {
        if (element.id == post.id) {
          element.dislikes++;
        }
      })
    },

    async fetchPosts(){
      try{
        const response = await axios.get('https://jsonplaceholder.typicode.com/posts');
        let posts = response.data;
        posts.forEach(post => {
          this.posts.push({
            id: post.id,
            title: post.title,
            body: post.body,
            likes: 0,
            dislikes: 0
          })
        })
      }catch(e){
        alert('Ошибка запроса')
      }
    }
  }
}
</script>

<style scoped>

</style>