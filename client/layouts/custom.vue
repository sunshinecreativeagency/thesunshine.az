<template lang="pug">
main.layout
  section.content 
    slot
</template>

<style lang="scss" scoped>
.layout {
  width: 100vw;
  height: 100vh;
  padding: 1rem 2rem;
}

</style>