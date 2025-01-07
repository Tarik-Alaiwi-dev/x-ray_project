<template>

  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand p-1">
        <router-link to="/" class="navbar-item"><strong>Pneumonia Detection System</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }">
        <div class="navbar-end">
          <router-link to="/log-out" class="button is-danger m-3"><span>Log Out</span></router-link>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2024</p>
    </footer>

  </div>

</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
    }
  },
  beforeCreate(){
    this.$store.commit('initializeStore')
    const token = this.$store.state.token

    if(token){
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else{
      axios.defaults.headers.common['Authorization'] = ""
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
