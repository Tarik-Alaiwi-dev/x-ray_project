<template>

  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">X-RAY</router-link>

        <a class="navbar-burger" aria-label="menu" aiara-expanded="false" data-target="navbar-menu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <router-link to="/log-out" class="button is-danger"><span>Log Out</span></router-link>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>

</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
