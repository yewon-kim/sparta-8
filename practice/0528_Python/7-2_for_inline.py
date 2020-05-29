# int/float list [1,2,3] -> [101, 102, 103]
students = range(1, 4)
students = [i + 100 for i in students]
print(students)

# str list를 각 길이로 변환
names = ["Waldo", "Sergey", "Nikolai", "Ilya"]
names = [len(i) for i in names]
print(names)

# str list를 upperCase로 변환
names = ["Waldo", "Sergey", "Nikolai", "Ilya"]
names = [i.upper() for i in names]
print(names)