<template>
    <div class="chatroom-form">
        <h4><span>채팅방 제목</span></h4><button type="button"><img src="../img/menu.png"></button>
        <ChatroomInputForm/>
    </div>
</template>
<script>
import ChatroomInputForm from '../components/ChatroomInputForm'
export default {
    name: 'ChatroomForm',
    components:{
        ChatroomInputForm
    }
}
</script>
<style scoped>
.chatroom-form{
   /* height:530vh; */
   position: fixed;
   left: 33%;
   top: 35%;
   width: 540px;
   height: 620px;
   margin: -165px 0 0 -228px;
   padding: 45px 60px 60px;
   background-color: #fff;
   border: 1px solid #ededed;
   border-radius: 2rem;
}
h4{
    display: inline;
}
button img{
    margin-left: 880%;
    height:30px;
    width:37px;
}
</style>