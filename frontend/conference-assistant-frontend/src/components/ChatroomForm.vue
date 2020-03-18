<template>
    <div class="chatroom-form">
        <h4><span>채팅방 제목</span></h4><button type="button"><img src="../img/menu.png"></button>
         <div class="page-container">
          <textarea class="textarea" v-model="textarea" disabled v-auto-scroll-bottom></textarea>
        <div class="input_div">
          <div class="file_input_div">
             <img src="../img/fileupload.png" class="file_input_img_btn" alt="open" />
             <input type="file" name="file_1" class="file_input_hidden" onchange="javascript: document.getElementById('fileName').value = this.value"/>
          </div>
           <div class="chat_input_div">
             <input type="text" v-model="message" @keyup.enter="sendMessage()" placeholder="채팅을 입력하세요."/>
             <button @click="sendMessage()">전송</button>
           </div>
        </div>
      </div>
    </div>
</template>
<script>
import ChatroomInputForm from '../components/ChatroomInputForm'
export default {
    name: 'ChatroomForm',

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
  width:80%
}
.page-container{
  height: 800px;
  width: 300px;
  border: 1px solid rgba(#000, .12);
}
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
   text-align:left;
}
input[type="text"]{
    font-size: 14px;
    margin-top: 10px;
    margin-bottom: 15px;
    margin-left:3%;
    padding-right: 50%;

}
.chat_input_div{
    margin-left: -5px;
    width:155%;
    height:54px;
    border : 1.5px solid rgba(202, 202, 202, 0.932);
    border-radius: 1rem;
}
.chat_input_div button{
    /* margin-left: 50%; */
    margin-top: 2px;
    height: 94%;
    width: 50px;
    border-radius: 0.5rem;
    background-color: #32a852;
    font-weight: 600;
    color:white;
}
.input_div{
    padding-top: 54%;
    font-size: 14px;
}
.file_input_div {
    position:fixed;
    margin-top: -5.7%;
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
    right:20px;
    top:110px;
    width:50px;
    opacity:0;
    filter: alpha(opacity=0);
    -ms-filter: alpha(opacity=0);
    cursor:pointer;
}

</style>