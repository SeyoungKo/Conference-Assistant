<template>
    <div class="chatroom-input-form">
        <input type="text" placeholder="   채팅을 입력하세요."/>
        <button type="submit">전송</button>
    </div>

</template>
<script>
export default {
    name : 'ChatroomInputForm'
}
</script>
<style scoped>
.chatroom-input-form{
   position:fixed;
   left:32%;
   top:105%;
   width: 518px;
   height:10%;
   margin: -165px 0 0 -205px;
   padding: 45px 60px 60px;
   background-color: rgb(223, 223, 223);
   border: 1px solid #ededed;
   border-radius: 0.8rem;
}
input[type="text"]{
    position:fixed;
    margin-left: -3%;
    margin-top: -11px;
    height:58px;
    width: 440px;
    border-radius: 0.3rem;
}
button[type="submit"]{
    position:fixed;
    margin-top: -11px;
    margin-left:380px;
    height:58px;
    width:60px;
    color:white;
    font-weight: 800;
    border-radius: 0.5rem;
    background:#32a852;
}
</style>