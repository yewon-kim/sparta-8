# 02. 역명을 치면 안내문구가 나오는 함수 (05/28)
def announce(station):
    print(station,"행 열차가 들어오고 있습니다.")
announce("강남")
announce("역삼")

# 03. 날짜를 무작위로 생성하는 함수 (05/28)
from random import *
month = randrange(1, 13)
def randomDate():
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = randrange(1, 32)
        print(month, "월", day, "일 입니다.")

    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = randrange(1, 31)
        print(month, "월", day, "일 입니다.")

    elif month == 2:
        day = randrange(1, 29)
        print(month, "월", day, "일 입니다.")

randomDate()

# 04. 사이트 별 비밀번호를 생성해주는 함수 (예: goo61!) (05/28)
def password(url):
    domain = url.split(".")[1]
    print(domain[:3] + str(len(domain)) + str(domain.count("e")) + "!")

password('http://www.naver.com/')
password('https://www.youtube.com/')

# 05. 1, 2, 3... 20번 중 1명은 치킨, 3명은 커피 쿠폰에 당첨시키는 함수 (05/28)
from random import *
users = list(range(1, 21))
winners = sample(users, 4)
print("CHICKEN: {0}".format(winners[0]))
print("COFFEE: {0}".format(winners[1:4]))

# 06. 승객 n명의 소요시간이 5~15분일 경우에만 태울 경우 총 탑승객 수를 구하는 함수 (05/29)
def passenger_list(n):
    count = 0
    for passenger in range(1, n + 1):
        time = randrange(1, 31)
        if 5 <= time <= 15:
            print("[O] {0}번 승객 (소요시간: {1}분)".format(passenger, time))
            count += 1
        else:
            print("[ ] {0}번 승객 (소요시간: {1}분)".format(passenger, time))
    print("총 탑승객 수:", count)

passenger_list(10)