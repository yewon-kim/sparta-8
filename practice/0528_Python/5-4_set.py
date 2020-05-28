# 집합
# #중복 안 됨, 순서 없음.
my_set = {1, 2, 3, 1, 2}
print(my_set)

# 표현 방법
A = {"a", "b", "c"}
B = set(["a", "1"])

# 교집합
print(A & B)
print(A.intersection(B))

# 합집합
print(A | B)
print(A.union(B))

# 차집합
print(A - B)
print(A.difference(B))

# 추가
A.add("d")
print(A)

# 제거
A.remove("d")
print(A)