<template>
    <div class="chat-topiclist-form">
         <!-- test data -->
            <div class="added-topic-div">
                <p>&nbsp;&nbsp;&nbsp;최종 보고서 작성하기</p>
                <hr style="border : 1px solid #eeeeee; margin-top:15px;">
            </div>
            <!-- ------- -->
            <button class="ok-btn" type="button" @click="close">OK</button>
    </div>
</template>
<script>
export default {
    name : 'ChatTopicListForm'
}
</script>
<style scoped>
hr{
    border :2px solid rgb(219, 219, 219);
}
.boundary-line-hr{
    border :16px solid #f7f7f7;
    margin-left: -60px;
    width:538px;
}
.added-topic-div{
    padding-top: 10px;
    margin-bottom: 5px;
    font-size:14px;
}
.ok-btn{
    height: 45px;
    width: 130px;
    margin-left: 35%;
    margin-top:35%;
    border-radius: 0.3rem;
    background-color: #32a852;
    font-weight: 600;
    color:white;
}
</style>