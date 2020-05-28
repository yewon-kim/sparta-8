from random import *

print(random()) # 0 이상 1 미만 임의의 실수 생성
print(random() * 10) # 0 이상 10 미만 임의의 실수 생성
print(int(random() * 10)) # 0 이상 10 미만 임의의 정수 생성
print(int(random() * 10) + 1) # 1 이상 11 미만 임의의 정수 생성
print(int(random() * 45) + 1) # 1 이상 46 미만 임의의 정수 생성
print(randrange(1, 46)) # 위와 같은 함수
print(randint(1, 45)) # 위와 같은 함수

date = randrange(4, 29)
print("모임 날짜는 매월 " + str(date) + "일 입니다.")