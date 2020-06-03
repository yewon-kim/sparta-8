from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    # 1. 클라이언트가 준 title, author, review 가져오기.
    title_recieve = request.form['title_give']
    author_recieve = request.form['author_give']
    review_recieve = request.form['review_give']

	# 2. DB에 정보 삽입하기
    review = {
        'title': title_recieve,
        'author': author_recieve,
        'review': review_recieve
    }
    db.reviews.insert_one(review)

	# 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '리뷰 작성 완료!'})
    

@app.route('/reviews', methods=['GET'])
def read_reviews():
		# 1. DB에서 리뷰 정보 모두 가져오기
    reviews = list(db.reviews.find({},{'_id':0}))
		# 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=15000, debug=True)