<template>
    <div class="main-page">
        <SidebarMenu/>
        <p>main page</p>
        <ChatroomForm/>
        <SelectedChatForm/>
        <AIKeywordListForm/>
    </div>
</template>
<script>
import SidebarMenu from '../components/SidebarMenu'
import ChatroomForm from '../components/ChatroomForm'
import SelectedChatForm from '../components/SelectedChatForm'
import AIKeywordListForm from '../components/AIKeywordListForm'

export default {
    name:'MainPage',
    components:{
        SidebarMenu,
        ChatroomForm,
        SelectedChatForm,
        AIKeywordListForm
    }
}
</script>
<style scoped>

</style>