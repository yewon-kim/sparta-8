### 재귀함수 : 함수 안에 자기 함수가 호출되는 것
# sum
def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

print(sum(10))

# factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# 문자열 역진행하며 한 글자씩 출력
def reverse_one(fruit):
    i = len(fruit) - 1
    while i >= 0 :
        letter = fruit[i]
        print(letter)
        i = i - 1

reverse_one("banana")