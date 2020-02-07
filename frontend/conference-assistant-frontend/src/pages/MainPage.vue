<template>
    <div class="main-page">
        <SidebarMenu/>
        <p>main page</p>
        <ChatroomForm/>
    </div>
</template>
<script>
import SidebarMenu from '../components/SidebarMenu'
import ChatroomForm from '../components/ChatroomForm'
export default {
    name:'MainPage',
    components:{
        SidebarMenu,
        ChatroomForm
    }
}
</script>
<style scoped>

</style>