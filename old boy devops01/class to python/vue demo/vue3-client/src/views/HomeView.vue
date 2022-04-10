<template>
  <div class="home">
<!--    <img alt="Vue logo" src="../assets/logo.png">-->
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
  <Nav/>


  </div>
</template>

<script>
// @ is an alias to /src
import Nav from '@/components/nav.vue'

export default {
  name: 'HomeView',
  components: {
    Nav,
  }
}
</script>
