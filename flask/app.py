import os
import sys
import os
from flask import Flask, render_template, session, jsonify
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit
import database
import model
import textrank

req_keyword = ''

app = Flask(__name__)
socketio = SocketIO(app, ping_timeout=2, cors_allowed_origins="*")

cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# 요청 키워드를 포함한 채팅 반환
@app.route('/keyword/<keyword>')
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def GET(keyword):
    req_keyword = keyword
    rtn_msgs =database.selected_chat(req_keyword)


    return jsonify(rtn_msgs)

@socketio.on('connect', namespace='/corekeyword') # namespace : 연결할 socket 식별
def connect():
    tmp = ''
    if textrank.rtn_keyword!= '' and tmp != textrank.rtn_keyword and textrank.sub_words !='':

        emit("response", {'message':'Connected', 'keyword':textrank.rtn_keyword, 'subwords':textrank.sub_words,'room_idx': '1'}) # socket 연결시 room_idx를 확인한다
        tmp = textrank.rtn_keyword

        @socketio.on('disconnect', namespace='/corekeyword')
        def disconnect():
            session.clear()
            print("Socket Disconnected")

        # disconnect()

@socketio.on("request", namespace='/coreKeyword')
def request(rtn_keyword):
    emit("response", {'message': model.rtn_keyword,'room_idx':'1'}, broadcast=True)

if __name__ == '__main__':
    model.main()
    app.run()


