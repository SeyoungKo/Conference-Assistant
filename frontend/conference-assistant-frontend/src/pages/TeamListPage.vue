<template>
    <div class="team-list-page">
        <AppHeader/>
        <img src="../img/profile.png">
        <div class="div-info">
            <span>user1</span>
            <p>user1@google.com</p>
        </div>
        <TeamList/>
    </div>
</template>
<script>
import TeamList from '../components/TeamList'
import AppHeader from '../components/AppHeader'
export default {
    name:'TeamListPage',
    components:{
        TeamList,
        AppHeader
    }
}
</script>
<style scoped>

img{
    margin-top: 110px;
    margin-left: 27px;
    width:93px;
    height:93px;

}
span{
    margin-left: 9%;
    margin-bottom: 4px;
    display: inline-block;
    color:black;
    font-size: 22px;
}
p{
    margin-left: 10%;
    color:black;
    font-size: medium;
}
.div-info{
    display:inline-block;
    margin-top: -14px;
}
</style>