# 1. Get name and age
# if age < 10, say "안녕"
# else if 10 <= age < 20, say "안녕하세요"
# else say "안녕하십니까"

def sayHello(name, age):
    if age < 10:
        print("안녕, " + name)
    elif age >=10 and age < 20:
        print("안녕하세요, " + name + " 학생")
    else:
        print("안녕하십니까, " + name + " 씨")

sayHello("도윤", 5)
sayHello("서준", 10)
sayHello("하준", 15)
sayHello("은우", 20)