<template>
    <div class="chatroom-input-form">
            <br>
            <p>채팅방 이름&nbsp;&nbsp;&nbsp;&nbsp;</p><input class="chatname-input" type="text"/>
            <br><br><hr>
            <span>회의 안건</span>
            <img class="add-topic" src="../img/add_topic.png">
            &nbsp;<input class="topic-input" type="text" placeholder="         추가할 회의 안건을 입력해주세요.">
            <br><br>
            <hr class="boundary-line-hr">
    </div>
</template>
<script>
export default {
    name : 'ChatroomInputForm'
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
.add-topic{
    padding-top: 10px;
    margin-left: 5%;
    width:22px;
    height:22px;
    position:absolute;
}
.topic-input{
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