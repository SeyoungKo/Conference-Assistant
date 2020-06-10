<template>
  <transition name="modal-fade">
    <div class="create-chat-alert-modal">
      <div class="modal"
        role="dialog"
        aria-labelledby="modalTitle"
        aria-describedby="modalDescription"
      >
        <header
          class="modal-header"
          id="modalTitle"
          >
            <span class="phrase"><p>채팅 방 이름 혹은 회의 안건을  <br>최소1개 이상 등록해주세요.</p></span>
        </header>
        <footer>
            <button type="button" class="btn-green" @click="btnok" aria-label="Close modal">OK</button>
        </footer>
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    name: 'CreateTeamModal',
    methods: {
      btnok() {
        this.$emit('btnok');
      }
    }
  };
</script>
<style scoped>
.modal-fade-enter,
  .modal-fade-leave-active {
    opacity: 0;
  }
  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: opacity .2s ease
  }
  .create-chat-alert-modal {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(141, 141, 141, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    height:30%;
    width:28%;
    border-radius: 0.5rem;
    background: rgb(250, 250, 250);
    box-shadow: 1px 1px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding-top: 55px;
    display: flex;
  }

  .modal-header {
    color:#32a852;
    font-size: 23px;
    text-align: center;
    font-weight: 800;
    margin-left: 22%;
    justify-content: space-between;
  }

  .phrase {
    text-align:center;
    font-weight: 600;
    font-size: 18px;
    color:rgb(105, 105, 105);
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    justify-content: flex-end;
  }

  button.btn-green {
    margin-top: 55px;
    margin-left: 150px;
    height:40px;
    width:25%;
    background: #32a852;
    font-size: 15px;
    color: #ffffff;
    font-weight: bold;
    border: 1px solid #32a852;
    border-radius: 0.3rem;
  }
</style>
</style>