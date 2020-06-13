<template>
    <div class="chat-topiclist-form">
        <div class="added-topic-div">
            <ChatroomInputForm @addChatInfo="addChatInfo"/>
                <ul class="topic-list">
                    <li v-for="(t, index) in info" :key="index" v-bind="handleChatInfo(t.topic, t.roomname)">
                        <div >{{t.topic}} </div>
                        <hr style="border : 1px solid #eeeeee; margin-top:15px;">
                    </li>
                </ul>
                <button class="ok-btn" type="button" @click="close">OK</button>
                <CreateChatAlertModal v-if="isModalVisible" @btnok="closeModal"></CreateChatAlertModal>
        </div>
    </div>
</template>
<script>
import ChatroomInputForm from './ChatroomInputForm'
import CreateChatAlertModal from '../modal/CreateChatAlertModal'

export default {
    name : 'ChatTopicListForm',
    components:{
        ChatroomInputForm,
        CreateChatAlertModal
    },
    data(){
        return{
            info:[],
            isModalVisible : false,
            roomname : '',
            topic : ''
        };
    },
    methods:{
        //***** */
        handleChatInfo(t,r){
            // this.topics.push(t);
            this.topic = t;
            this.roomname  = r;
        },
        addChatInfo(payload){
            this.info.push(payload);

            // const last = this.info.slice(-1);

            // for(var i=0; i<this.info.length; i++){
            //     for(var j=0; j<this.info[i]['topic'].length; j++){
            //         this.topics.push(this.info.roomname[i]['topic'][j]);
            //         // this.roomname = this.info.roomname[this.info.length -1];
            //     }
            // }
            // this.roomname = payload[0].roomname
        },
        close(){
            if(this.topic != '' && this.roomname !=''){

                this.$emit('submit', {
                    topic : this.topic,
                    roomname : this.roomname
                });
                localStorage.setItem(this.roomname, this.topic);
            }else{
                this.showModal()
            }
        },
        showModal(){
            this.isModalVisible = true;
        },
        closeModal(){
            this.isModalVisible = false;
        }
    }
}
</script>
<style scoped>
.topic-list{
    height: 180px;
   overflow-y:scroll;
}
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
    margin-left: 75%;
    border-radius: 0.3rem;
    background-color: #32a852;
    font-weight: 600;
    color:white;
    /* position 하단 고정 */
    position: fixed;
    bottom: 2rem;
    left: 0;


}
</style>