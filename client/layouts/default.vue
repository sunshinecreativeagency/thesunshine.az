<script>
import Sidebar from '../components/sidebar.vue'

export default {
  components: {
    Sidebar
  }  
}
</script>

<template lang="pug">
main.layout
  section.content 
    slot
  Sidebar
</template>

<style lang="scss" scoped>
.layout {
  width: 100vw;
  height: 100vh;
  display: grid;
  grid-template-columns: 2fr 1.5fr; 
  grid-template-rows: auto; 
  gap: 10px;
  padding: 1rem 2rem; 
}

</style>