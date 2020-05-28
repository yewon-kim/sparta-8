# str hello
hello = "Hello, World!"

# lower(), upper(), isupper(), islower()
print(hello.lower())
print(hello.upper())
print(hello[0].isupper())
print(hello[0].islower())

# len()
print(len(hello)) # 길이

# replace()
print(hello.replace("Hello", "Hi"))

# index(), find()
index = hello.index("o")
print(index) # 첫 번째 "o"의 위치
index = hello.index("o", index + 1)
print(index) # 두 번째 "o"의 위치
print(hello.find("o")) # 첫 번째 "o"의 위치
print(hello.find("x")) # "x" 없으면 return -1 (index에서는 오류)

# count()
print(hello.count("o")) # 개수 세기

# strip()
text = "       text       "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# split()
print(hello.split()) # 공백을 기준으로 array 정렬

email = "example@domain.com"
print(email.split("@"))
print("ID:",email.split("@")[0])
print("Domain:",email.split("@")[1].split(".")[0])