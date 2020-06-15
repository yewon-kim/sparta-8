from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

import re

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def star_list():
    # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    stars = list(db.mystar.find({},{'_id':False}).sort('like',-1))
    # 2. 성공하면 success 메시지와 함께 stars 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success','stars_list':stars})

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

@app.route('/api/add', methods=['POST'])
def saving():
	# 1. 클라이언트로부터 데이터를 받기
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    comment_receive = cleanhtml(comment_receive)
    find_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', comment_receive)
    for str_link in find_url: comment_receive = comment_receive.replace(str_link, "<a target = \"_blank\" href = \"" + str_link + "\" >" + str_link + "</a>")

	# 2. meta tag를 스크래핑하기
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')

    url_image = og_image['content']
    url_title = og_title['content']

    article = {
        'name': cleanhtml(url_title),
        'img_url': cleanhtml(url_image),
        'recent': comment_receive,
        'url': cleanhtml(url_receive),
        'like': 0
    }

	# 3. mongoDB에 데이터를 넣기
    db.mystar.insert_one(article)
    
    return jsonify({'result': 'success', 'msg':'포스팅 되었습니다!'})

@app.route('/api/like', methods=['POST'])
def star_like():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    name_receive = request.form['name_give']

    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    star = db.mystar.find_one({'name':name_receive})
    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    new_like = star['like']+1

    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    # 참고: '$set' 활용하기!
    db.mystar.update_one({'name':name_receive},{'$set':{'like':new_like}})

    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})


@app.route('/api/delete', methods=['POST'])
def star_delete():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    name_receive = request.form['name_give']
    # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
    db.mystar.delete_one({'name':name_receive})
    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)