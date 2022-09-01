<template>
  <form @submit.prevent class="post-form">
    <h2> Create post</h2>
    <input-field :label="title" :id="formTitle" v-model="post.title" required/>
    <input-field :label="body" :id="formBody" v-model="post.body" required/>
    <base-button @click="createPost">Create</base-button>
  </form>
</template>

<script>
import InputField from "@/components/UI/BaseInput";
import BaseButton from "@/components/UI/BaseButton";

export default {
  name: "PostForm",
  components: {
    InputField,
    BaseButton
  },
  data(){
    return {
      post: {
        title:  '',
        body: '',
        likes: 0,
        dislikes: 0
      },
      formTitle: 'form-title',
      formBody: 'form-description',
      title: 'Title',
      body: 'Description'
    }
  },
  methods: {
    createPost() {
      this.post.id = Date.now()
      this.$emit('create', this.post)
      this.post = {
        title: '',
        body: '',
        likes: 0,
        dislikes: 0
      }
    }
  }
}
</script>

<style scoped>
.post-form input{

}
</style>