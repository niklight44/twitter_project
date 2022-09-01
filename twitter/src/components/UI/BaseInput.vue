<template>
  <div class="mb-3">
    <label class="form-label" :for="id">{{ label }}</label>
    <input type="text" class="form-contol"  :id="id" @input="updateInput">
  </div>
</template>

<script>
export default {
  name: "InputField",
  props: {
    modelValue: String,
    label: {
      type: String,
      required: true
    },
    id: {
      type: String,
      required: true
    }
  },
  methods: {
    updateInput(event){
      this.$emit('update:modelValue', event.target.value)
    }
  }
}
</script>

<style scoped>
.form-label{
  display:block;
}
</style>