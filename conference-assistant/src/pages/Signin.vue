<template>
    <div class="sign-in-page">
      <h3 style="text-align:center">로그인</h3>
      <SigninForm/>
    </div>
</template>
<script>
import SigninForm from '../components/SigninForm'
export default {
    name:'Signin',
    components:{
        SigninForm
    }
}
</script>
<style scoped>

</style>