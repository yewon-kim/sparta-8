dictionary = {1: "하나", 2: "둘"}

# 가져오기
print(dictionary[1])
print(dictionary.get(2))
print(dictionary.get(5)) # None
print(dictionary.get(5, "현재 value 없음")) # None 대신 출력

# key 있는지 검증
print(1 in dictionary) # True
print(3 in dictionary) # False

# 변경, 추가
dictionary[1] = "one"
dictionary[3] = "셋"
print(dictionary)

# 삭제
del dictionary[3]
print(dictionary)

# 출력
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

# 비우기
dictionary.clear()
print(dictionary)