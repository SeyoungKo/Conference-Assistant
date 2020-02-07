<template>
    <div class="sign-in-page">
      <h3 style="text-align:center">로그인</h3>
      <SigninForm @submit="onSubmit"/>
    </div>
</template>
<script>
import SigninForm from '../components/SigninForm'
// import {mapActions} from 'vuex'
export default {
    name:'Signin',
    components:{
        SigninForm
    },
    methods:{
        onSubmit(){
                alert('로그인이 완료되었습니다.');
                this.$router.push({name:'TeamListPage'})
        }
    }
}
</script>
<style scoped>

</style>