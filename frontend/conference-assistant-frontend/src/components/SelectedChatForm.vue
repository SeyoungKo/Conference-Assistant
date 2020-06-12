<template>
    <div class="selected-chat-form">
        <div v-if="clicked == false">
            <p class="p-checkinfo">키워드를 선택하면 회의 내용이 보여집니다.</p>
        </div>
        <div class="div-msg">
            <p class="p-selectedKeyword">{{selected_keyword}}</p><p class="p-msg">{{info_msg}}</p>
        </div>
        <div v-for="(m, index) in msg" :key="index">
            <span class="span-selectedUser">user1</span><p class="p-selectedMsg">{{m}}</p>
        </div>
        <p v-if="!msg.length && clicked==true" class="p-nullMsg">선택한 키워드에 대한 회의 내용이 없습니다.</p>
    </div>
</template>
<script>
import {EventBus} from '../EventBus'

export default {
    name: 'SelectedChatForm',
    data(){
        return{
            selected_keyword:' ',
            key_index : '',
            info_msg : '',
            clicked : false,
            msg : '',
        }
    },
    beforeMount(){
    EventBus.$on('event', (obj)=>{
           this.selected_keyword = '\'' + obj.keyword + '\''
           this.info_msg = '에 대한 회의 내용입니다.'
           this.msg = obj.msg

           if(this.clicked == false){
               this.clicked = !this.clicked
           }
        })
    }
}
</script>
<style scoped>
.selected-chat-form{
   position: fixed;
   left: 75%;
   top: 35%;
   width: 570px;
   height: 220px;
   margin: -165px 0 0 -228px;
   padding: 45px 60px 60px;
   background-color: #fff;
   border: 1px solid  #eeeeee;
   box-shadow: 4px 4px 2px rgb(233, 233, 233);
   border-radius: 1.2rem;
   overflow-y: scroll;
}
.p-checkinfo{
    text-align:center;
    margin-top:10%;
    font-size: 16px;
    color:rgb(168, 168, 168);
}
.p-selectedKeyword{
    margin-top:-10px;
    display: inline-block;
    color: #69a77a;
    font-weight: 750;
    font-size: 19px;
}
.p-msg{
    display: inline-block;
    font-weight: 750;
    font-size: 19px;
}
.p-selectedMsg{
    line-height:20px;
    margin-top: 10px;
    background: #ececec;
    font-size: 14px;
    width:96%;
    margin-left:-5%;
    padding: 4px 4px;
    padding-bottom: 2%;
    color:#646464;
    border-radius: 0.3rem;
    display:inline-block;
}
.div-msg{
    padding:10 10 10 10;
    margin-left: -2%;
    padding-top: -3%;
    position: fixed;

    top:105px;
    width:100%;
}
.p-nullMsg{
    padding-top:14%;
    text-align: center;
    font-size : 16px;
    color: rgb(168, 168, 168);
}
.span-selectedUser{
    color:#646464;
    background: #ececec;
    margin-left :-9%;
    padding: 4px 4px;
    padding-bottom: 5px;
    margin-right: 7%;
    border-radius: 0.3rem;

}
</style>