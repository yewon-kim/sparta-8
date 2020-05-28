weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈":
    print("우산 챙기세요")
elif weather == "미세먼지":
    print("마스크 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("더위에 주의하세요.")
elif 10 <= temp < 30:
    print("괜찮은 날씨예요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("추위에 주의하세요.")