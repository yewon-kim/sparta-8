from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from bs4 import BeautifulSoup

import requests
import re
import datetime
from time import time

from bson import ObjectId

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
    stars = list(db.mystar.aggregate([
        {'$set': {'_id': {'$toString': '$_id'}}},
        {'$sort': {'like': -1}}
    ]))

    # 2. 성공하면 success 메시지와 함께 stars 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success','stars_list':stars})



def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def regex_search_group(string, regex):
    pattern = re.compile(regex)
    m = pattern.search(string)
    if m : return m.group()
    else: return None

regex_url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

@app.route('/api/add', methods=['POST'])
def saving():
	# 1. 클라이언트로부터 데이터를 받기
    comment_receive = request.form['comment_give']
    url_receive = regex_search_group(comment_receive, regex_url)

    comment_receive = cleanhtml(comment_receive)
    find_url = re.findall(regex_url, comment_receive)
    for str_link in find_url: comment_receive = comment_receive.replace(str_link, "<a target = \"_blank\" href = \"" + str_link + "\" >" + str_link + "</a>")

	# 2. meta tag를 스크래핑하기
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')

    url_image = 'https://upload.wikimedia.org/wikipedia/commons/6/6a/A_blank_flag.png' if og_image == None else og_image['content']
    url_title = url_receive if og_title == None else og_title['content']

    article = {
        'time': time(),
        'name': cleanhtml(url_title),
        'img_url': cleanhtml(url_image),
        'comment': comment_receive,
        'url': cleanhtml(url_receive),
        'like': 0
    }

	# 3. mongoDB에 데이터를 넣기
    db.mystar.insert_one(article)
    
    return jsonify({'result': 'success', 'msg':'포스팅 되었습니다!'})

@app.route('/api/like', methods=['POST'])
def star_like():
    objectid_receive = request.form['objectid_give']
    star = db.mystar.find_one({'_id':ObjectId(objectid_receive)})
    new_like = star['like']+1
    db.mystar.update_one({'_id':ObjectId(objectid_receive)},{'$set':{'like':new_like}})

    return jsonify({'result': 'success'})


@app.route('/api/delete', methods=['POST'])
def star_delete():
    objectid_receive = request.form['objectid_give']
    db.mystar.delete_one({'_id':ObjectId(objectid_receive)})

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)