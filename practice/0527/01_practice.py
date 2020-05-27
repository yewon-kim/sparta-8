import requests 

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

for gu in r.json()['RealtimeCityAir']['row']:
    name = gu['MSRSTE_NM']
    if gu["NO2"] < 0.015:
        print("지역: ", name, " 이산화질소 농도: 낮음")
    elif gu["NO2"] == 0.015:
        print("지역: ", name, " 이산화질소 농도: 보통")
    else:
        print("지역: ", name, " 이산화질소 농도: 높음")