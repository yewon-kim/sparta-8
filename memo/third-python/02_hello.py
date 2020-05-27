import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()['RealtimeCityAir']['row']
for gu in rjson:
	name = gu['MSRSTE_NM']
	level = gu["IDEX_MVL"]
	if level < 60:
		print(name, level, " 좋음")
	else:
		print(name, level, " 나쁨")

for province in rjson:
	time = province["MSRDT"]
	name = province["MSRSTE_NM"]
	coLevel = province["CO"]
	print("기준시각:", time, name, "일산화탄소 농도:", coLevel)