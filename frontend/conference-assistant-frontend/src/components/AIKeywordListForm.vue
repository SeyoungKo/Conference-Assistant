<template>
    <div class="aikeyword-list-form">
        <h4>AI가 찾은 키워드</h4>

         <div v-if="keywords && keywords.length >0">
            <div class="keywords" v-for="(keyword, index) in rtn_keywords" :key="index" >
                <span>{{keyword}}</span>
            </div>
         </div>
    </div>
</template>
<script>
import SocketIo from 'socket.io-client'
export default {
    name: 'AIKeywordListForm',
    data(){
        return {
            room_idx : '',
            keywords : [],
            socket : null,
            keyword : '',
            rtn_keywords : []
        }
    },
    props:{
      server:{
          type : String,
          required : true
      }
    },
    methods:{
        newSocket(){
            let socket = SocketIo(this.$props.server,{
                origins : 'http://localhost:*/* http://127.0.0.1:*/*'
            })
            this.socket = socket
            this.socket.on('response', (data)=>{
                if(data.room_idx.length !=0){
                this.keywords = [...this.keywords,data];

                this.doMath(this.keywords);
              }
            })
        },
        doMath(keywords){
            var arr = new Array();

            if(this.keywords != ''){
                for(var i=0; i<this.keywords.length; i++){
                    for(var j=0; j<this.keywords[i]['keyword'].length; j++){

                            arr= arr.concat(this.keywords[i]['keyword'][j]);
                            let filteredArray = arr.filter((item, index)=> // 중복 제거
                                arr.indexOf(item) === index
                            );
                            this.rtn_keywords = filteredArray;
                      }
                 }
                return this.rtn_keywords;
            }
        }
    },
    mounted(){
        this.newSocket()
    }
}
</script>
<style scoped>
.aikeyword-list-form{
   position: fixed;
   left: 97%;
   top: 68%;
   width: 250px;
   height: 380px;
   margin: -165px 0 0 -228px;
   padding: 45px 60px 60px;
   background-color: #fff;
   border: 1px solid  #eeeeee;
   box-shadow: 4px 4px 2px rgb(233, 233, 233);
   border-radius: 1.2rem;
   overflow-y:scroll;
}
h4{
    margin-top:-20%;
    margin-left: -30%;
    font-size: 20px;
    font-weight: 700;
}
p{
    padding-top: 70%;
    margin-left: -20%;
    color:gray;
    width:300px;
}
</style>