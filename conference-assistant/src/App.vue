<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import AppHeader from './components/AppHeader'
export default {
  name: 'App',
  components:{
    AppHeader
  }
}
</script>

<style>
/* @import 'http://localhost:8080/assets/index.css'; */
@import 'assets/index.css';
</style>
