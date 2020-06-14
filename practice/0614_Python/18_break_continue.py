# break: 0 ~ 10 정수 출력하기
i = 0
while True:
    print(i)
    i += 1
    if i > 10:
        break

for i in range(100):
    print(i)
    if i == 10:
        break

# continue: 0 ~ 10 중 짝수(0 제외) 출력
i = 0
while i <= 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

for i in range(10):
    if i % 2 != 0:
        continue
    print(i + 2)

# break 응용
count = int(input('반복할 횟수를 입력하세요 >> '))
# for i in range(count):
#     print(i)

i = 0
while True:
    print(i)
    i += 1
    if i == count:
        break

# Quiz: 1 ~ 100 중 3으로 끝나는 숫자 출력
for i in range(100):
    if i % 10 != 3:
        continue
    print(i, end=" ")

i = 0
while True:
    i += 1
    if i % 10 != 3:
        continue
    if i > 100:
        break
    print(i, end=" ")