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

# index HTML
@app.route('/')
def home():
    return render_template('index.html')

# index API
@app.route('/api/top', methods=['GET'])
def show_all_top():
    # 1. articles 목록 전체를 검색합니다. happy 가 많은 순으로 정렬합니다.
    articles = list(db.database.aggregate([
        {'$set': {'_id': {'$toString': '$_id'}}},
        {'$sort': {'happy': -1}}
    ]))

    # 2. 성공하면 articles 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success', 'articles_list': articles})

@app.route('/api/new', methods=['GET'])
def show_all_new():
    articles = list(db.database.aggregate([
        {'$set': {'_id': {'$toString': '$_id'}}},
        {'$sort': {'time': -1}}
    ]))
    return jsonify({'result': 'success', 'articles_list': articles})


# category HTML
@app.route('/<isoCode>')
def category(isoCode):
    return render_template('category.html', isoCode = isoCode)

# category API
@app.route('/api/top/<isoCode>', methods=['GET'])
def show_category_top(isoCode):
    articles = list(db.database.aggregate([
        {'$set': {'_id': {'$toString': '$_id'}}},
        {'$match': {'category_code': isoCode}},
        {'$sort': {'happy': -1}}
    ]))
    return jsonify({'result': 'success', 'articles_list': articles})

@app.route('/api/new/<isoCode>', methods=['GET'])
def show_category_new(isoCode):
    articles = list(db.database.aggregate([
        {'$set': {'_id': {'$toString': '$_id'}}},
        {'$match': {'category_code': isoCode}},
        {'$sort': {'time': -1}}
    ]))
    return jsonify({'result': 'success', 'articles_list': articles})


# article HTML
@app.route('/<isoCode>/<articleId>')
def article(isoCode, articleId):
    return render_template('article.html', isoCode = isoCode, articleId = articleId)

# article API
@app.route('/api/<articleId>', methods=['GET'])
def show_article(articleId):
    article = list(db.database.aggregate([
        {'$set': {'_id': {'$toString': '$_id'}}},
        {'$match': {'_id': articleId}},
    ]))
    return jsonify({'result': 'success', 'article': article})

# POST API
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

@app.route('/api/postarticle', methods=['POST'])
def post_article():
	# 1. 클라이언트로부터 데이터를 받기
    category_code_receive = request.form['category_code_give']
    post_body_receive = request.form['post_body_give']
    url_receive = regex_search_group(post_body_receive, regex_url)

    if url_receive == None:
        article = {
        'category_code': category_code_receive,
        'time': time(),
        'post_body': post_body_receive,
        'url_title': '',
        'url_img': '',
        'url': '',
        'happy': 0
        }

        db.database.insert_one(article)
        
        return jsonify({'result': 'success', 'msg':'포스팅 되었습니다!'})

    else:
        post_body_receive = cleanhtml(post_body_receive)
        find_url = re.findall(regex_url, post_body_receive)
        for str_link in find_url: post_body_receive = post_body_receive.replace(str_link, "<a target = \"_blank\" href = \"" + str_link + "\" >" + str_link + "</a>")

        # 2. meta tag를 스크래핑하기
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url_receive, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')

        og_image = soup.select_one('meta[property="og:image"]')
        og_title = soup.select_one('meta[property="og:title"]')

        url_image = 'https://upload.wikimedia.org/wikipedia/commons/6/6a/A_blank_flag.png' if og_image == None else og_image['content']
        url_title = url_receive if og_title == None else og_title['content']

        article = {
            'category_code': category_code_receive,
            'time': time(),
            'post_body': post_body_receive,
            'url_title': cleanhtml(url_title),
            'url_img': cleanhtml(url_image),
            'url': cleanhtml(url_receive),
            'happy': 0
        }

        # 3. mongoDB에 데이터를 넣기
        db.database.insert_one(article)
        
        return jsonify({'result': 'success'})


@app.route('/api/happy', methods=['POST'])
def happy():
    objectid_receive = request.form['objectid_give']
    article = db.database.find_one({'_id':ObjectId(objectid_receive)})
    new_happy = article['happy'] + 1
    db.database.update_one({'_id':ObjectId(objectid_receive)},{'$set':{'happy':new_happy}})

    return jsonify({'result': 'success', 'article_happy': article['happy']})

@app.route('/api/delete', methods=['POST'])
def star_delete():
    objectid_receive = request.form['objectid_give']
    db.database.delete_one({'_id':ObjectId(objectid_receive)})

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)