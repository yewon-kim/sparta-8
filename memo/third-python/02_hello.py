import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

for gu in r.json()['RealtimeCityAir']['row']:
	name = gu['MSRSTE_NM']
	level = gu["IDEX_MVL"]
	if level < 60:
		print(name, level, " 좋음")
	else:
		print(name, level, " 나쁨")
