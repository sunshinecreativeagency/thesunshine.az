<script>
import feather from 'feather-icons'

definePageMeta({
  layout: "custom",
})

export default {
  data() {
    return {
      socials: [
        {
          to: "#",
          text: "Mail"
        },
        {
          to: "#",
          text: "LINKEDIN"
        },
        {
          to: "#",
          text: "X"
        },
        {
          to: "#",
          text: "INSTAGRAM"
        },
        {
          to: "#",
          text: "Facebook"
        },
      ],
    }
  },
  mounted() {
    feather.replace()
  }
}
</script>

<template lang="pug">
section.wrapper 
  aside.sidebar
    .about
      header.header 
        h1.title About

      section.content 
        p Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae labore dolorem reprehenderit repellat pariatur deserunt totam ipsa et veritatis culpa ut eum obcaecati, quia tempora, sed, repellendus iste autem earum?
        span.alt-text since 2024


    ul.social
      li(v-for="link in socials" :key="link.to")
        NuxtLink(:to="link.to").badge {{ link.text }}

    NuxtLink(to="/").close-btn 
      i(data-feather="x")
</template>


<style lang="scss" scoped>

  .wrapper {
    width: 100%;
    height: calc(100vh - 2rem);
    display: flex;
    justify-content: flex-end;

    .sidebar {
      position: relative;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      justify-content: space-between;
      padding: 2rem 1rem;
      border-radius: 1.5625rem;
      background-color: #000;
  
      .about {
        color: #fff;

        .content {
          width: 50%;
        }

        .alt-text {
          text-decoration: underline;
        }
      }

      .social {
        display: flex;
        justify-content: flex-end;
        gap: .5rem;
  
        .badge {
          color:#fff;
          border-color: #fff;
        }
      }

      .close-btn {
        position: absolute;
        right: 1.5rem;
        top: 1.5rem;
        background: none;
        border: none;
        color: #fff;

        .feather {
          width: 2rem;
          height: 2rem;
        }
      }
    }
  }
</style>