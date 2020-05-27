import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rows = r.json()['RealtimeCityAir']['row']
for gu in rows:
	name = gu['MSRSTE_NM']
	level = gu["IDEX_MVL"]
	if level < 60:
		print(name, level, " 좋음")
	else:
		print(name, level, " 나쁨")

for province in rows:
	time = province["MSRDT"]
	region = province["MSRRGN_NM"]
	name = province["MSRSTE_NM"]
	coLevel = province["CO"]
	print("기준시각:", time, region, name, "일산화탄소 농도:", coLevel)

for gu in rows:
	time = gu["MSRDT"]
	name = gu['MSRSTE_NM']
	level = gu["IDEX_MVL"]
	print("기준일자: ", time)
	if level < 60:
		print(name, level, " 좋음")
	else:
		print(name, level, " 나쁨")

for gu in rows:
    name = gu['MSRSTE_NM']
    if gu["NO2"] < 0.015:
        print("지역: ", name, " 이산화질소 농도: 낮음")
    elif gu["NO2"] == 0.015:
        print("지역: ", name, " 이산화질소 농도: 보통")
    else:
        print("지역: ", name, " 이산화질소 농도: 높음")