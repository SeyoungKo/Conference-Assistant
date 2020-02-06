<template>
    <div class="team-list-page">
<<<<<<< HEAD
        <AppHeader/>
=======
>>>>>>> frontend
        <img src="../img/profile.png"><span>user1</span>
        <p>user1@google.com</p>
        <TeamList/>
    </div>
</template>
<script>
import TeamList from '../components/TeamList'
<<<<<<< HEAD
import AppHeader from '../components/AppHeader'
export default {
    name:'TeamListPage',
    components:{
        TeamList,
        AppHeader
=======
export default {
    name:'TeamListPage',
    components:{
        TeamList
>>>>>>> frontend
    }
}
</script>
<style scoped>
img{
    margin-top: 10%;
    margin-left: 20px;
}
span{
    position: absolute;
    margin-left: 2%;
    margin-top: 11%;
    color:black;
    font-size: 22px;
}
p{
    position: absolute;
    margin-left: 10%;
    margin-top: -3%;
    color:black;
    font-size: medium;
}
</style>