<template>
    <div class="chatroom-input-form">
     <!-- <div class="input_div">
        <div class="file_input_div">
            <img src="../img/fileupload.png" class="file_input_img_btn" alt="open" />
            <input type="file" name="file_1" class="file_input_hidden" onchange="javascript: document.getElementById('fileName').value = this.value"/>
        </div>
            <textarea v-model="message" rows="5" placeholder="   채팅을 입력하세요."/>
            <button type="button" @click="onSubmit">전송</button>
        </div> -->
    </div>
</template>

<script>
export default {
    name : 'ChatroomInputForm',

    onSubmit(){
        const{message}= this
        this.$emit('submit', message)
        this.message=''
    }
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
/* input[type="text"]{
    position:fixed;
    margin-left: -3%;
    margin-top: -11px;
    height:58px;
    width: 440px;
    border-radius: 0.3rem;
} */
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

.input_div{
    margin-top: 80%;
}

</style>