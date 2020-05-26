x = [4,2,1,3]
a = ["hello", "world"]

print(x)

num_elements = len(x) # list의 element 개수
print(num_elements)

y = sorted(x) # 순서대로 정렬한 list
print(y)

z = sum(x) # list 내의 숫자 합
print(z)

for n in x: # list의 element를 차례로 print
    print(n)
for b in a:
    print(b)

print(x.index(4)) # index()의 parameter가 list 내 몇 번째에 있는지 print
print(a.index("world"))

print("hello" in a) # parameter가 list 내 있는지 True of False로 print
if "hello" in a:
    print("list a에 hello가 있어요!")