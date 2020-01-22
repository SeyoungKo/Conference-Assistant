<template>
    <div class="sign-up-page">
        <h3 style="text-align:center"><span style="color:#32a852">두레</span> 회원가입</h3>
        <SignupForm/>
    </div>
</template>
<script>
import SignupForm from '../components/SignupForm'
export default {
    name:'Signup',
    components:{
        SignupForm
    }
}
</script>
<style scoped>

</style>