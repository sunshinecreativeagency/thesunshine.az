<template>
    <NuxtLayout>
      <NuxtPage/>
    </NuxtLayout>
</template>

<style lang="scss">
  *, *::before, *::after {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }

  ul {
    list-style: none;
  }

  a {
    text-decoration: none;
  }

  .badge {
    color: #000;
    padding: 0.5rem 1rem;
    border: 1px solid #000;
    border-radius: 1rem;
  }

  .badge-fill {
    background-color: #000;
  }
</style>