list = ["a", "b", "c"]

print(list.index("c"))

list.append("d")
print(list)

list.insert(1, "a")
print(list)

list.pop() # 맨 뒤의 것만 뽑아냄
print(list)

print(list.count("a"))

# 숫자 리스트 정렬
num_list = [7, 3, 6, 2, 5]

num_list.sort() 
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear() # 전부 삭제
print(num_list)

# extend()
num_list = [7, 3, 6, 2, 5]
mix_list = ["text", 10, True]
num_list.extend(mix_list)
print(num_list)