<template>
    <div class="app-header">
     <img src="../img/dure_logo.png"><span>Dure</span>
     <router-link :to="{name:'Signin'}">로그아웃</router-link>
    </div>
</template>
<script>
export default {
    name : 'AppHeader'
}
</script>
<style scoped>
.app-header{
  position: fixed;
   top: 0;
   left: 0;
   width: 100%;
   height: 70px;
   border-bottom: 1px solid #ededed;
   background-color: rgb(255, 255, 255);
}
img{
    margin: 13px 10px;
    width: 40px;
    height: 40px;
}
span{
    position:fixed;
    margin-top: 19px;
    font-size: 25px;
    font-weight: bold;
    color: #63c29a
}
a{
   position: fixed;
   margin-top: 30px;
   margin-left: 90%;
   color:rgb(31, 31, 31);
}
</style>