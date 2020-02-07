<template>
    <div class="team-list">
        <router-link :to="{name: 'Signup'}">프로필 변경</router-link>
        <button type="button">팀 추가하기</button>
    </div>
</template>
<script>
export default {
    name : 'TeamList'
}
</script>
<style scoped>
.team-list a{
  float:left;
  height: 10%;
   width: 13%;
   margin-top: -5%;
   margin-left: 80%;
   margin-bottom: 20%;
   padding: 1rem;
   font-size: 19px;
   font-weight: bold;
   text-align: center;
   color: #fff;
   border-radius: 2rem;
   background-color: #32a852;
   text-decoration: none;
   transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}
.team-list button[type="button"]{
    margin-left: 4%;
    margin-top: -20%;
    height: 10%;
    width: 90%;
    padding: 2rem;
    font-size: 19px;
    font-weight: bold;
    text-align: center;
    color: #fff;
    border-radius: 1rem;
    background-color: #cacaca;

}

</style>