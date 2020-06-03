# Flask
from flask import Flask, render_template
app = Flask(__name__)

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!', "title": title_receive})

# route 같아도 method가 다르면 동일 route 가능!
@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!', "title": title_receive})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)

# 0.0.0.0 / localhost = 127.0.0.1
# for Mac / for Windows

# 터미널에서 Ctrl + C 누르면 종료됨

# https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=a
# 주소 : search.naver.com
# 경로 : /search.naver
# 쿼리 파라미터 : sm=top_hty&fbm=1&ie=utf8&query=a

# https://search.naver.com/search.naver/movies
# 주소 : search.naver.com
# 경로 : /search.naver/movies
# 쿼리 파라미터 : 없음

# http://localhost:27017/
# 주소 : search.naver.com
# 경로 : / (루트 PATH)
# 쿼리 파라미터 : 없음