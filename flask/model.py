import os
import re
import threading

import textrank

from numpy import matrix
from pymongo import MongoClient

from soynlp.tokenizer import RegexTokenizer
from time import sleep
from konlpy.tag import Okt

client = MongoClient()
# 클래스 객체 할당

matrix = []

client = MongoClient('mongodb://localhost:27017/local')

count =0
text=''
rtn_keyword = ''
noun_list=''


# 쓰레드로 가져온 최근 값

# DB_HOST = 'XXX.XX.XX.XXX:27017'
# DB_ID = 'root'
# DB_PW = 'PW'
# client = MongoClient('mongodb://%s:%s@%s' % (DB_ID, DB_PW, DB_HOST))


class AsyncTask:

    def __init__(self):
        pass

    def TaskA(self):

        rtn_messages = ""
        arr = [20]
        MAX_TEXTLEN=100
        count =0

        db = client["local"]
        # db 객체 할당받기

        chats = db["chats"]
        # db에서 collection 이름으로 객체를 생성

        coll = db.chats

        coll_list = db.list_collection_names()


        # 채팅을 1000글자 단위로 저장한다.
        while (1):
            sleep(2)

            cursor = db.chats.find().sort([('created_at', -1)]).limit(1)
            docs = list(cursor)
            last_message = docs[0]["contents"]
            arr.append(last_message)

            if count>2 and arr[count-1] != arr[count]:
                rtn_messages += last_message

            docs.clear()
            print(rtn_messages, len(rtn_messages), "count:", count)

            count +=1

            if len(rtn_messages) >= MAX_TEXTLEN:
                # 새로운 리스트에 누적 채팅 1000개를 만들기 위해 저장한다.
                text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', rtn_messages)

                tokenizer = RegexTokenizer()

                # 명사 빈도 추출
                textrank.init(text)
                tr = textrank.TextRank()
                tr.build()
                tr.extract()

                rtn_keyword = textrank.kw
                print("rtn_keyword:", rtn_keyword)
                break

        threading.Timer(3,self.TaskA).start()

def main():
    count =0
    at = AsyncTask()
    at.TaskA()


if __name__ =='__main_':
    main()
# res = json.dumps(chats, default=str)
# json 직렬화 (serialize)

# chats collection에서 불러온 json타입 데이터에서 contents 문자열 가져오기

# def cleanText(rtn_chats):a
#     for msg in (str)(rtn_chats.values()):
#         text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '',msg)
#         print(text)
#         return text

# cleanText(chats)

