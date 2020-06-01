### Built-in 내장함수

# input : 사용자 입력을 받는 함수
user = input("이름을 입력해 주세요: ")
print("환영합니다, {0} 님.".format(user))

# dir : 어떤 object를 넘겨줬을 때, 그 object가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # module 외장함수
print(dir())
print(dir(random))

lst = [1, 2, 3]
print(dir(lst))

string = "John"
print(dir(string))