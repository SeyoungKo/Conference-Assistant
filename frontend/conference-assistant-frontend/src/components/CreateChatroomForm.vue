<template>
<transition name="form-fade">
    <div class="create-chatroom-form">
            <h3>채팅방 생성</h3>
            <img class="close-img" src="../img/close.png" @click="close">
            <!-- <ChatroomInputForm/> -->
            <ChatTopicListForm @close="close"/>
    </div>
</transition>
</template>
<script>
import ChatTopicListForm from './ChatTopicListForm'

export default {
    name : 'CreateChatroomForm',
    components:{
        ChatTopicListForm
    },
    methods:{
        close(){
            this.$emit('close');
        }
    }
}
</script>
<style scoped>
.form-fade-enter,
.form-fade-leave-active{
    opacity:0;
}
.form-fade-enter-active,
.form-fade-leave-active{
    transition: opacity .3s ease
}
.create-chatroom-form{
   position: fixed;
   left: 75%;
   top: 35%;
   width: 570px;
   height: 615px;
   margin: -165px 0 0 -228px;
   padding: 45px 60px 60px;
   background-color: #fff;
   border: 1px solid  #eeeeee;
   box-shadow: 4px 4px 2px rgb(233, 233, 233);
   border-radius: 1.2rem;
}
h3{
    top:10px;
    font-size: 20px;
    text-align:center;
}
.close-img{
    position:absolute;
    top:25px;
    margin-left: 82%;
    width:18px;
    height:18px;
}

p:nth-child(9){
    padding-top: 10px;
    text-align: center;
    font-weight: 500;
}

::placeholder{
    font-size:15px;
    font-weight: 500;
}

</style>