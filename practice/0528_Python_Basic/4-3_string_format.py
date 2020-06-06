print("a" + "b") # 붙여쓰기
print("a", "b") # 띄어쓰기

# Format 1
print("나는 %d살." % 20) # 정수
print("내 이름은 %s." % "코난") # string
print("Conan의 두문자는 %c." % "C") # character (1글자)
print("내 이름은 %s, %s이죠." %("코난", "탐정")) # 여러 개

# Format 2
print("나는 {}살입니다.".format(20))
print("내 이름은 {}, {}이죠.".format("코난", "탐정"))
print("내 이름은 {0}, {1}이죠.".format("코난", "탐정")) # 순서
print("내 이름은 {1}, {0}이죠.".format("코난", "탐정")) # 순서

# Format 3
print("내 이름은 {name}, {job}이죠.".format(name = "코난", job = "탐정"))