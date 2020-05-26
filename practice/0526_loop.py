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

# for문과 continue
for i in range(3):
    print(i)
    print("John: Hi, Jane. How are you doing?")
    print("Jane: Hi, John. I'm fine.")
    if i == 1: # 이 조건이 True라면
        continue # (아래 코드는 건너뛰고) 다음 i의 조건 확인을 계속.
    print("Alex: Hi, John, Jane!") # if 조건이 False인 경우들만 출력됨

for i in range(10): # i = 0부터 시작해서 1씩 더한 10개의 숫자 중
    if i % 3 == 1: # 3로 나눈 나머지가 1이라면
        continue # 거르고
    print(i) # 아니라면 출력

marks = [90, 25, 42, 75, 83]
num = 0
for mark in marks:
    num = num + 1
    if mark < 60:
        continue # 60점 미만 거르라는 뜻
    print("축하합니다! %d번 학생 합격입니다." % num)

# for문과 range 응용
add = 0
for i in range(1, 11):
    add = add + i
print(add)

scores = [93, 46, 86, 65, 23]
for i in range(len(scores)):
    if scores[i] < 60:
        continue
    print("%d번 학생 합격입니다." % (i + 1))

for i in range(2, 10): # i는 2 이상 10 미만
    for j in range(1, 10): # j는 1 이상 10 미만
        print(i * j, end = " ") # end = " "는 한 칸 띄고 옆에 출력
    print('') # Enter 효과

scores = [93, 46, 86, 65, 23]
for i in range(len(scores)):
    if scores[i] < 60:
        print("%d번 성적: F" % (i + 1))
    elif scores[i] < 90 and scores[i] >= 60:
        print("%d번 성적: B" % (i + 1))
    elif scores[i] >= 90:
        print("%d번 성적: A" % (i + 1))

number = 0
for score in scores:
    number = number + 1
    if score < 60:
        print("%d번 성적: F" % number)
    elif score < 90 and score >= 60:
        print("%d번 성적: B" % number)
    elif score >= 90:
        print("%d번 성적: A" % number)