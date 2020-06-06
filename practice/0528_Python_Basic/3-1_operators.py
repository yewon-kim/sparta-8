print(1 + 1) # 2
print("A" + "b") # Ab
print(2*2) # 4
print(7/3) # 2.33333...

print(2 ** 3) # 8
print(5 % 3) # 2 (나머지)
print(5 // 3) # 1 (몫)

print(3 == 3) # True
print(10 > 3) # True
a = 3
print(a == 3) # True

print(1 != 1) # False (같지 않다)
print(not(1 != 1)) # True

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 4) or (3 < 5)) # True
print((3 > 4) | (3 < 5)) # True (\+shift == |)

b = 4
print(0 < b <= 2) # False

number = 10
print(number)   # 10
number = number + 2
print(number)   # 12
number += 2
print(number)   # 14
number -= 2
print(number)   # 12
number %= 5
print(number)   # 2