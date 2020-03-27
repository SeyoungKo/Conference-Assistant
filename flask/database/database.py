from pymongo import MongoClient
import datetime

client = MongoClient()
# 클래스 객체 할당

client = MongoClient('mongodb://localhost:27017/local')

# DB_HOST = 'XXX.XX.XX.XXX:27017'
# DB_ID = 'root'
# DB_PW = 'PW'
# client = MongoClient('mongodb://%s:%s@%s' % (DB_ID, DB_PW, DB_HOST))

db = client["mongo_tutorial"]
# db 객체 할당받기

users = db["users"]
# db에서 collection 이름으로 객체를 생성

post={
    "id" : "mike",
    "age" : 20,
    "text" : "테스트 도큐먼트입니다1."
}

coll = db.users
# users 변수에 해당하는 collection 이름으로 할당된다.
coll.insert(post)

coll_list = db.collection_names()
# collection 목록 보기

for post in coll.find():print(post)
# users에 저장된 도큐먼트 모두 불러오기

