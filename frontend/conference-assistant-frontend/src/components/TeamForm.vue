<template>
    <div class="team-form">
         <router-link clsss="router-main" :to="{name: 'MainPage', params:{teamname : teamname}}">
            <div class="team-item" v-for="(team, index) in teamlist" :key="index" @click="selectedTeamname(team)">
                <img class="close" src="../img/close.png">
                <img class="img-teamprofile" src="../img/dure_team_profile.png">
                <p class="team-name">{{team}}</p><br>
                <p style="margin-left:100px; font-size:14px; color:black; margin-top:-5px;">http://{{team}}.dure.com</p>
            </div>
        </router-link>
    </div>
</template>
<script>
export default {
    name : 'TeamForm',
    props : ['teamlist'],
    data(){
        return{
            teamname : ''
        }
    },
    methods:{
        selectedTeamname(team){
            this.teamname = team
        }
    }
}
</script>
<style scoped>
    .team-item{
        margin-top: 10px;
        margin-bottom: 20px;
        margin-left: 90px;
        width: 85%;
        border : 1.5px solid rgb(223, 223, 223);
        background: #ffffff;
        border-radius: 0.4rem;
        height: 90px;
    }
    .img-teamprofile{
        margin-top: -27px;
        width:90px;
        height:90px;
    }
    .close{
        margin-top: 5px;
        margin-left: 98%;
        display:block;
        width:21px;
        height:21px;
    }
    .team-name{
        margin-top: -80px;
        margin-left: 120px;
        font-size: 22px;
        font-weight: 600;
        color:rgb(59, 59, 59);
    }
</style>