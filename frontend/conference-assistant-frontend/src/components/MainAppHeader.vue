<template>
    <div class="main-app-header">
        <img src="../img/default_profile.png"/>
            <router-link :to="{name:'Signin'}">&nbsp;user1</router-link>
    </div>
</template>
<script>
export default {
    name : 'MainAppHeader'
}
</script>
<style scoped>
    .main-app-header{
        margin-top: -20px;

    }
    img{
        margin-top:-10px;
        margin-left: 90%;
        width:46px;
        height:45px;
        vertical-align: middle;
    }
    a{
        margin-left: 6px;
        color:rgb(59, 59, 59);
        font-size:19px;
        font-weight: 400;

    }

</style>