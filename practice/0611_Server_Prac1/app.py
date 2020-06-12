from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/api/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    articles = list(db.prac1.find({}, {'_id': 0}))

    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'articles': articles})

## API 역할을 하는 부분
@app.route('/api/memo', methods=['POST'])
def saving():
	# 1. 클라이언트로부터 데이터를 받기
    name_receive = request.form['name_give']
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

	# 2. meta tag를 스크래핑하기
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_image = og_image['content']
    url_title = og_title['content']
    url_description = og_description['content']

    article = {'name': name_receive, 'url': url_receive, 'comment': comment_receive, 'image': url_image,
               'title': url_title, 'desc': url_description, 'like': 0}
    
	# 3. mongoDB에 데이터 넣기
    db.prac1.insert_one(article)

    return jsonify({'result': 'success'})

@app.route('/api/like', methods=['POST'])
def like_article():
    # 1. 클라이언트가 전달한 number_give를 number_receive 변수에 넣습니다.
    number_receive = request.form['number_give']

    # 2. db에서 find_one으로 number이 number_receive와 일치하는 article을 찾습니다.
    article = db.prac1.find_one({'number': number_receive})

    # 3. article의 like 에 1을 더해준 new_like 변수를 만듭니다.
    new_like = article['like'] + 1

    # 4. db목록에서 number이 number_receive인 문서의 like 를 new_like로 변경합니다.
    # 참고: '$set' 활용하기!
    db.prac1.update_one({'number':number_receive}, {'$set':{'like':new_like}})

    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg':'좋아요!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)