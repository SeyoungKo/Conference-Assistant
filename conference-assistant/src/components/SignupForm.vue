<template>
    <div class="sign-up-form">
        <!--HTML5에서 자체적인 유효성 검사를 하지 않도록 수동 설정 -->
        <form @submit.prevent="submit" novalidate>
            <fieldset>
                 <span>아이디 </span><input v-model="id" type="text" placeholder="아이디를 입력해주세요."/><button>&nbsp;&nbsp;중복확인</button><br>
                 <span>비밀번호 </span><input v-model="password" type="password" placeholder="비밀번호를 입력해주세요."/><br>
                 <span>비밀번호 확인 </span><input v-model="passwordConfirm" type="password" class="confirm" placeholder="비밀번호를 한번 더 입력해주세요."/><br>
                 <span>이름 </span><input type="text" class="name" v-model="name" placeholder="이름을 입력해주세요."/><br>
                 <span>전화번호 </span><input type="text" class="tel" v-model="tel" placeholder="전화번호를 입력해주세요."/><br>
                 <span>이메일 </span><input type="email" v-model="email" placeholder="이메일을 입력해주세요."/>
                <button type="submit">회원가입</button>
            </fieldset>
        </form>
    </div>
</template>
<script>
export default {
    name:'SignupForm',
    data(){
        return{
            id:'',
            password:'',
            passwordConfirm:'',
            name:'',
            tel:'',
            email:''
        }
    },
    methods:{
        submit(){
            const {id, password, passwordConfirm, name, tel, email} = this
            if(!id || !password || !passwordConfirm || !name || !tel || !email){
                alert('모든 항목을 입력해주세요.');
                return;
            }
            if(password != passwordConfirm){
                alert('비밀번호가 일치하지 않습니다.');
                return;
            }
            this.$emit('submit',{id, password, passwordConfirm, name, tel, email})
        }
    }
}
</script>
<style scoped>

</style>