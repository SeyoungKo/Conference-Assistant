<template>
    <div class="sign-in-form">
       <form @submit.prevent="submit">
           <fieldset>
               <input type="text" placeholder="아이디를 입력하세요."/>
               <input type="password" placeholder="비밀번호를 입력하세요."/>
               <div></div>
               <p><input type="checkbox"/><span> 로그인 상태 유지</span></p>
               <div></div>
               <button type="submit">Login</button>
               <div><p>비밀번호가 생각나지 않으세요?</p></div>
               <button>Join</button>

           </fieldset>
       </form>
    </div>
</template>
<script>
export default {
    name: 'SigninForm'
}
</script>
<style scoped>


</style>f