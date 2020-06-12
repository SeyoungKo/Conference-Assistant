<template>
<transition name="form-fade">
    <div class="create-chatroom-form">
            <h3>채팅방 생성</h3>
            <img class="close-img" src="../img/close.png" @click="exit">

            <ChatTopicListForm @submit="submit"/>
    </div>
</transition>
</template>
<script>
import ChatTopicListForm from './ChatTopicListForm'
import axios from 'axios'
import {EventBus} from '../EventBus'

// import api from '@/api'

// const APIcore = axios.create({
//     baseURL : '//localhost:8080/roominfo'
// })
export default {
    name : 'CreateChatroomForm',
    data(){
        return{
            rtn_roomname : '',
            rtn_topic : ''
        }
    },
    components:{
        ChatTopicListForm
    },
    methods:{
        submit(topic, roomname){

            // axios.post('http://127.0.0.1:5000/roominfo/'+ `${topics}`, topics).then(res=>{
            //     this.rtn_input = res.data
            // })

            // this.rtn_roomname = roomname;
            // this.rtn_topic = topic;

            EventBus.$emit('chatinfo', {
                info : topic,
                roomname : roomname
            })
            this.$emit('close');
        },
        exit(){
            this.$emit('exit');
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