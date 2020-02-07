<template>
    <div class="sign-up-form">
        <!--HTML5에서 자체적인 유효성 검사를 하지 않도록 수동 설정 -->
        <h3 style="text-align:center">두레 회원가입</h3>
        <form @submit.prevent="submit" novalidate>
            <fieldset>
                <p>아이디 </p><input type="text" placeholder="아이디를 입력해주세요."/><button>중복확인</button>
                <p>비밀번호 </p><input type="password" placeholder="비밀번호를 입력해주세요."/>
                <p>이름 </p><input type="text" placeholder="이름을 입력해주세요."/>
                <p>전화번호 </p><input type="text" placeholder="전화번호를 입력해주세요."/>
                <p>이메일 </p><input type="text" placeholder="이메일을 입력해주세요."/>

                <button type="submit">회원가입</button>
            </fieldset>
        </form>
    </div>
</template>
<script>
export default {
    name:'SignupForm'
}
</script>
<style scoped>

</style>