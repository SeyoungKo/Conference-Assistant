<template>
    <div class="chatroom-form">
        <h4 class="chat-title"><span>채팅방 제목</span></h4><button type="button"><img src="../img/menu.png"></button>
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
   z-index:0;
   position: fixed;
   margin-top:1.8%;
   width: 580px;
   height: 610px;
   margin-left: 17%;
   box-shadow: 4px 4px 2px rgb(233, 233, 233);
   background-color: #fff;
   border: 1px solid #eeeeee;
   border-radius: 1.2rem;
}
.chat-title{
    display: inline;
    margin-left: 20px;
    font-size: 18px;
    display:inline-block;
}
button img{
    margin-left: 999%;
    margin-top:20px;
    padding-left: 10%;
    height:30px;
    width:37px;
}
.textarea{
  height:420px;
  margin-left: 10%;
  margin-bottom: -130px;
  width:163%
}
.page-container{
  height: 700px;
  width: 300px;
  border: 1px solid rgba(#000, .12);
}
.chatroom-input-form{
   position:fixed;
   left:40%;
   top:105%;
   width: 600px;
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
    padding-right: 54.5%;

}
.chat_input_div{
    margin-left: 48px;
    width:165%;
    height:56px;
    border : 1px solid rgba(184, 184, 184, 0.932);
    border-radius: 1rem;
}
.chat_input_div button{
    /* margin-left: 50%; */
    height: 100%;
    width: 58px;
    margin-left: 0.5px;
    border-radius: 0.4rem;
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
    height:25px;
    margin-left: 30%;
    margin-top: 353%;
    padding:0 0 0 5px;
}
.file_input_hidden {
    position: absolute;
    margin-left: 50%;
    margin-top:-10px;
    right:-15px;
    top:110px;
    width:50px;
    opacity:0;
    filter: alpha(opacity=0);
    -ms-filter: alpha(opacity=0);
    cursor:pointer;
}

</style>