from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

from time import time

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/comments/list', methods=['POST'])
def write_comment():
    name_receive = request.form['name_give']
    opinion_receive = request.form['opinion_give']

    comment = {
        'time': int(100000 * time()), 
        'name': name_receive, 
        'opinion': opinion_receive, 
        'like': 0
    }

    db.comments.insert_one(comment)

    return jsonify({'result':'success'})


@app.route('/comments/list', methods=['GET'])
def read_comments():
    # db에서 코멘트 정보 가져오기
    comments = list(db.comments.find({}, {'_id': 0}))

    # 성공 여부 & 코멘트 목록 반환
    return jsonify({'result':'success', 'comments': comments})


@app.route('/comments/like', methods=['POST'])
def like_comment():
    time_receive = request.form['time_give']
    comment = db.comments.find_one({'time': time_receive})
    new_like = comment['like'] + 1
    db.comments.update_one({'time': time_receive}, {'$set':{'like': new_like}})

    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)