<template>
    <div class="minutes-list-form">
        <h3>&nbsp;&nbsp;&nbsp;&nbsp;회의록 목록</h3>
            <select name="minutes-sort">
            <option value="">이름순</option>
            <option value="등록일자">등록일자</option>
            <option value="위치">위치</option>
        </select>
        <!-- sample data -->
        <div class="minutes-list">
            <div class="minutes-item"><p class="chatname-p">{{roomname}} #1</p>
                <p class="content-p">{{title}} </p>
                <p class="sub-content-p">&nbsp;&nbsp;&nbsp;&nbsp;생성일 : {{moment().format('MM-DD HH:mm')}}</p>
            </div>
        </div>
        <!--  -->
        <div class="clicked-minutes">
            <button class="delete-btn" type="text">삭제</button>
            <div class="clicked-contents-div">
                <h2>회의명 : {{roomname}}&nbsp;#1</h2>
                <h2 class="agenda-h2">회의 안건 :</h2><span>{{title}}</span>
                <h2>회의 일시 : {{moment().format('YYYY년 MM월 DD일')}}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                &nbsp;&nbsp;&nbsp;&nbsp;13:00-14:00</h2>
                <hr>
                <textarea>{{contents}}</textarea>
            </div>
        </div>

    </div>
</template>
<script>
import moment from 'vue-moment'
export default {
    name : 'MinutesListForm',
    created(){
        const title = this.$route.params.info.title;
        const contents = this.$route.params.info.contents;
        const roomname = this.$route.params.info.roomname;

        this.title = title;
        this.contents = contents;
        this.roomname = roomname;
    },
    data(){
        return{
            title :'',
            contents:'',
            roomname : ''
        }
    }
}
</script>
<style scoped>
.minutes-list-form{
   z-index:0;
   position: fixed;
   margin-top:1.8%;
   width: 1100px;
   height: 610px;
   margin-left: 19%;
   box-shadow: 4px 4px 2px rgb(233, 233, 233);
   background-color: #fff;
   border: 1px solid #eeeeee;
   border-radius: 1.2rem;
}
h3{
    margin-top:40px;
    font-size:24px;
}
select{
    margin-left: 20px;
    margin-top:15px;
    width: 150px;
    padding: .8em .5em;
    border: 1px solid rgb(223, 223, 223);
    font-family: inherit;
    background: url('../img/select_drop.png') no-repeat 93% 30%;
    border-radius: 0px;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
}
.minutes-item{
    margin-top:20px;
    margin-left:20px;
    width:42%;
    height:25%x;
    background-color: #f0f0f0;
    box-shadow: 4px 7px 2px rgb(223, 223, 223);
    border-radius:0.2rem;
}
.content-p{
    margin-left: 20px;
    font-size:18px;
    font-weight: 700;
}
.sub-content-p{
    margin-left: 60%;

}
.chatname-p{
    padding-top:10px;
    margin-left: 20px;
    margin-bottom:8px;
    color:rgb(139, 139, 139);
    font-weight: 700;
    font-size: 17px;
}
.clicked-minutes{
   position: fixed;
   left: 75%;
   top: 45%;
   width: 460px;
   height: 510px;
   margin: -165px 0 0 -228px;
   padding: 45px 60px 60px;
   background-color: #fff;
   border: 1px solid  #e2e2e2;
   border-radius: 1.2rem;
}
.delete-btn {
    position:absolute;
    margin-top:-23%;
    left:76%;
    border: none;
    font-size: 100%;
    padding: 15px;
    width:100px;
    cursor: pointer;
    border-radius: 0.3rem;
    font-weight: 700;
    color: white;
    background: #32a852;
}
.agenda-h2{
    display:inline;
}
.clicked-contents-div{
    margin-top:-45px;
    margin-left:-50px;
    font-size:12px;
}
hr{
    border :1px solid #c5c5c5;
    margin-left: -10px;
    width:458px;
}
textarea{
    height:350px;
    width:110%;
    font-size:15px;
    font-weight:500;
    color:rgb(104, 104, 104);
}
</style>