<script>

export default {
  name: "Sidebar",
  data() {
    return {
      navlink: [
        {
          to: "/",
          text: "Home"
        },
        {
          to: "/blogs",
          text: "Blogs"
        },
        {
          to: "/projects",
          text: "Projects"
        },
        {
          to: "/about",
          text: "About"
        },
      ],
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
      phone: "(077) 305 42 56"
    }
  }
}
</script>

<template lang="pug">
aside.sidebar
  nav.navbar
    ul.menu
      li(v-for="link in navlink" :key="link.to")
        NuxtLink(:to="link.to").menu-item {{ link.text }}

  section.contact
    span {{ phone }}

  ul.social
    li(v-for="link in socials" :key="link.to")
      NuxtLink(:to="link.to").badge {{ link.text }}
    
</template>

<style lang="scss" scoped>
  .sidebar {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    justify-content: space-between;
    padding: 2rem 1rem;
    border-radius: 1.5625rem;
    background-color: #000;

    .navbar {
      .menu {
        .menu-item {
          color:#fff;
          font-size: 2.5rem;
        }
      }
    }
 
    .contact {
      flex: 1;
      color: #fff;
      font-size: 1.25rem;
    }

    .social {
      display: flex;
      gap: .5rem;

      .badge {
        color:#fff;
        border-color: #fff;
      }
    }
  }
</style>