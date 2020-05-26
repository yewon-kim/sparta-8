# for, while

for i in range(3):
    print(i)
    print("John: Hi, Jane. How are you doing?")
    print("Jane: Hi, John. I'm fine.")

i = 0
while i < 3:
    print(i)
    print("John: Hi, Jane. How are you doing?")
    print("Jane: Hi, John. I'm fine.")
    i = i + 1

i = 0
while True:
    print(i)
    print("John: Hi, Jane. How are you doing?")
    print("Jane: Hi, John. I'm fine.")
    i = i + 1
    if i > 2:
        break

for i in range(3):
    print(i)
    print("John: Hi, Jane. How are you doing?")
    print("Jane: Hi, John. I'm fine.")
    if i == 1: # 이 조건이 True라면
        continue # (아래 코드는 건너뛰고) 다음 i의 조건 확인을 계속.
    print("Alex: Hi, John, Jane!") # if 조건이 False인 경우들만 출력됨

for i in range(10): # i = 0부터 시작해서 1씩 더한 10개의 숫자 중
    if i % 2 == 0: # 2로 나눈 나머지가 0이라면
        print(i) # i를 출력

for i in range(10):
    if i % 2 == 1:
        continue
    print(i) # 2로 나눈 나머지가 1이 아닌 i를 출력