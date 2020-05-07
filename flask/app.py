import os
import sys
import os
from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit

import model

# sys.path.insert(0,"model.py")


app = Flask(__name__)
socketio = SocketIO(app, ping_timeout=2, cors_allowed_origins="*")

@socketio.on('connect', namespace='/corekeyword') # namespace : 연결할 socket 식별
def connect():
    tmp = ''
    if model.rtn_keyword!= '' and tmp != model.rtn_keyword:
        emit("response", {'message':'Connected', 'keyword':model.rtn_keyword, 'room_idx': '1'}) # socket 연결시 room_idx를 확인한다
        tmp = model.rtn_keyword

        @socketio.on('disconnect', namespace='/corekeyword')
        def disconnect():
            session.clear()
            print("Socket Disconnected")

        disconnect()

@socketio.on("request", namespace='/coreKeyword')
def request(rtn_keyword):
    emit("response", {'message': model.rtn_keyword,'room_idx':'1'}, broadcast=True)

if __name__ == '__main__':
    model.main()
    app.run()


