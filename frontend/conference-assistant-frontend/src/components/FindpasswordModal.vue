<template>
  <transition name="modal-fade">
    <div class="find-password-modal">
      <div class="modal"
        role="dialog"
        aria-labelledby="modalTitle"
        aria-describedby="modalDescription"
      >
        <header
          class="modal-header"
          id="modalTitle"
          >
          <slot name="header" class="representative-phrase-p">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;
            비밀번호가 생각나지 않으세요?
            <button
              type="button"
              class="btn-close"
              @click="close"
              aria-label="Close modal"
            ></button>
          </slot>
        </header>
        <section
          class="modal-body"
          id="modalDescription"
        >
          <slot name="body">
            <p >비밀번호를 전송받을 이메일을 입력하세요.</p>
            <input type="email" placeholder="  이메일을 입력해주세요."/>
          </slot>
        </section>

        <footer class="modal-footer">
          <slot name="footer">
            <button type="button" class="btn-green" @click="close" aria-label="Close modal">확인</button>
            <button type="button" class="btn-gray" @click="close" aria-label="Close modal">취소</button>
          </slot>
        </footer>
      </div>
    </div>
  </transition>
</template>
<script>
  export default {
    name: 'modal',
    methods: {
      close() {
        this.$emit('close');
      },
    },
  };
</script>
<style>
.modal-fade-enter,
  .modal-fade-leave-active {
    opacity: 0;
  }

  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: opacity .3s ease
  }
  .find-password-modal {
    position: fixed;
    margin-top:-80px;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    height:30%;
    width:60%;
    margin:15%;
    border-radius: 0.8rem;
    background: rgb(235, 235, 235);
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    border-bottom: 1px solid #eeeeee;
    color: rgb(63, 63, 63);
    font-size: 18px;
    font-weight: bold;
    margin-left: 25%;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    justify-content: flex-end;
  }

  .modal-body {
    position: relative;
    padding: 20px 10px;
  }

  p{
    margin-left: -5%;
    text-align: center;
    margin-top: -11%;
  }
  .btn-close {
    border: none;
    font-size: 100%;
    padding: 20px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

.modal-body input[type="email"]{
  margin-top: 5%;
  margin-left: 2%;
  height: 30px;
  border-radius: 0.5rem;
  width: 95%
}

button.btn-gray {
    margin-top: -20px;
    margin-left: 17%;
    height:39%;
    width:18%;
    background: rgb(173, 173, 173);
    font-size: 18px;
    color: #f3f2f2;
    font-weight: bold;
    border: 1px solid rgb(173, 172, 172);
    border-radius: 0.7rem;
  }
  button.btn-green {
    margin-top: -20px;
    margin-right: -175px;
    height:39%;
    width:18%;
    background: #32a852;
    font-size: 18px;
    color: #f3f2f2;
    font-weight: bold;
    border: 1px solid #32a852;
    border-radius: 0.7rem;
  }
  ::placeholder{
    font-size:14px;
  }
</style>