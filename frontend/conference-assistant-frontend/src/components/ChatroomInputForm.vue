<template>
    <div class="chatroom-input-form">
            <form @submit.prevent="addChatInfo">
                <br>
                <p>채팅방 이름&nbsp;&nbsp;&nbsp;&nbsp;</p><input class="chatname-input" v-model="roomname" type="text"/>
                <br><br><hr>
                <span>회의 안건</span>

                &nbsp;<input class="topic-input" type="text" v-model="topic" placeholder="         추가할 회의 안건을 입력해주세요.">
                 <br><br>
                <button type="submit"><img class="add-topic" src="../img/add_topic.png"></button>
               <hr class="boundary-line-hr">
            </form>

    </div>
</template>
<script>
export default {
    name : 'ChatroomInputForm',
    data(){
        return{
            topic : '',
            roomname:''
        };
    },
    methods:{
        resetField(){
            this.topic='';
        },
        addChatInfo(){
            const {topic, roomname} = this;
            const isEmpty = topic.length <=0 ;
            if(isEmpty){
                return false;
            }
            this.$emit('addChatInfo', {topic, roomname});
            this.resetField();
        }
    }
}
</script>
<style scoped>
.chatname-input{
    padding: 15px 25px 10px 10px;
    border: 1px solid #dfdfdf;
    border-radius: 0.5rem;
    height: 45px;
    width: 345px;
}
img.add-topic{
    margin-top: -50px;
    margin-left: -65px;
    width:22px;
    height:22px;
}
button{
    background: #ffffff;
    margin-left: 55%;
}
.topic-input{
    padding-top:20px;
    margin-left: 20px;
    padding: 15px 25px 10px 10px;
    width: 355px;
    /* font-size:00px; */
}
::placeholder{
    font-size:15px;
    font-weight: 500;
}
.boundary-line-hr{
    border :16px solid #f7f7f7;
    margin-left: -60px;
    width:538px;
}
p:nth-child(2){
    padding-top: 50px;
    display: inline;
    font-weight: 500;
}
span{
    font-weight: 500;
}
hr{
    border :0.01rem solid rgb(231, 231, 231);
}
</style>