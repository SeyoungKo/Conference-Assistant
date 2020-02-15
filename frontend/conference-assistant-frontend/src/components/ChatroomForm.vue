<template>
    <div class="chatroom-form">
        <h4><span>채팅방 제목</span></h4><button type="button"><img src="../img/menu.png"></button>
         <div class="page-container">
          <textarea class="textarea" v-model="textarea" disabled v-auto-scroll-bottom></textarea>
        <div class="file_input_div">
            <img src="../img/fileupload.png" class="file_input_img_btn" alt="open" />
            <input type="file" name="file_1" class="file_input_hidden" onchange="javascript: document.getElementById('fileName').value = this.value"/>
        </div>
        <input v-model="message" placeholder="   채팅을 입력하세요."/>
        <button @click="sendMessage()">전송</button>
    </div>
    </div>
</template>
<script>
import ChatroomInputForm from '../components/ChatroomInputForm'
export default {
    name: 'ChatroomForm',
    // components:{
    //     ChatroomInputForm
    // },
    created(){
        this.$socket.on('chat', (data)=>{
            this.textarea += data.message + '\n'
        })
    },
    data(){
        return{
            textarea : "",
            message : '',
        }
    },
    methods: {
        sendMessage(){
            this.$socket.emit('chat',{
                message: this.message
            });
            this.textarea += this.message +'\n'
            this.message = ''
        }
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
   box-shadow: 4px 4px 2px rgb(233, 233, 233);
   background-color: #fff;
   border: 1px solid #eeeeee;
   border-radius: 1.2rem;
}
h4{
    display: inline;
}
button img{
    margin-left: 880%;
    height:30px;
    width:37px;
}
.textarea{
  height:300px;
}
.page-container{
  height: 800px;
  width: 300px;
  border: 1px solid rgba(#000, .12);
}
/* ------ */
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
.file_input_div {
    position:fixed;
    margin-top: -10%;
}
.file_input_img_btn {
    overflow: hidden;
    width:22px;
    height:28px;
    margin-left: -170%;
    margin-top: 385%;
    padding:0 0 0 5px;
}
.file_input_hidden {
    position: absolute;
    margin-left: 100%;
    right:-150px;
    top:110px;
    opacity:0;
    filter: alpha(opacity=0);
    -ms-filter: alpha(opacity=0);
    cursor:pointer;
}

</style>