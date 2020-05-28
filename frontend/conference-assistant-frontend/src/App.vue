<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import AppHeader from './components/AppHeader'
import SidebarMenu from './components/SidebarMenu'

export default {
  name: 'App',
  components:{
    AppHeader,
    SidebarMenu
  },
  metaInfo() {
      return {
          title: "Epiloge - Build your network in your field of interest",
          meta: [
              { name: 'description', content:  'Epiloge is about connecting in your field of interest. Our vision is to help people share their knowledge, work, projects, papers and ideas and build their network through what they do rather where they live, study or work.'},
              { property: 'og:title', content: "Epiloge - Build your network in your field of interest"},
              { property: 'og:site_name', content: 'Epiloge'},
              {property: 'og:type', content: 'website'},
              {name: 'robots', content: 'index,follow'}
          ]
      }
  }
}
</script>

<style>
/* @import 'http://localhost:8080/assets/index.css'; */
@import 'assets/index.css';
</style>
