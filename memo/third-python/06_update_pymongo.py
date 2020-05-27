from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 생김새
db.users.update_many({'name': 'bobby'},{'$set': {'age': 999}})

# 예시 - 오타가 많으니 이 줄을 복사해서 씁시다!
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'bobby'})
print(user)

db.users.delete_one({'name':'bobby'})

user = db.users.find_one({'name':'bobby'})
print(user)