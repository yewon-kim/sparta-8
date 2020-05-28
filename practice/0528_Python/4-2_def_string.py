hello = "Hello, Waldo!"
print(hello.lower())
print(hello.upper())
print(hello[0].isupper())
print(len(hello)) # str의 길이
print(hello.replace("Waldo", "Sergey")) # str 내 값 변환

index = hello.index("o")
print(index) # 첫 번째 "o"의 위치
index = hello.index("o", index + 1)
print(index) # 두 번째 "o"의 위치

print(hello.find("o")) # 첫 번째 "o"의 위치
print(hello.find("x")) # "x"의 위치가 없으면 return -1 (index 쓰면 오류남)

print(hello.count("o")) # "o"의 개수