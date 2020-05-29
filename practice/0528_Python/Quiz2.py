# 03. 날짜를 무작위로 생성하는 함수
from random import *
month = randrange(1, 13)
def randomDate():
    if month == 2:
        day = randrange(1, 29)
        print("{0}월 {1}일입니다.".format(month, day))
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = randrange(1, 31)
        print("{0}월 {1}일입니다.".format(month, day))
    else:
        day = randrange(1, 32)
        print("{0}월 {1}일입니다.".format(month, day))
randomDate()

# 04. 사이트 별 비밀번호를 생성해주는 함수 (예: goo61!)
def password(url):
    domain = url.split(".")[1]
    print(domain[:3] + str(len(domain)) + str(domain.count("e")) + "!")
password("http://www.naver.com/")
password("http://www.google.com/")

# 05. 20명 중 1명은 치킨, n명은 커피 쿠폰에 당첨시키는 함수
def raffle(n):
    users = range(1, 20)
    winners = sample(users, n + 1)
    print("CHICKEN:", winners[0])
    print("COFFEE:", winners[1:])
raffle(3)
raffle(6)

# 05-1. n명 중 1명을 뽑는 함수
def show(n):
    print("당첨:", randint(1, n))
show(21)