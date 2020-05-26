# {key: value}

x = {
    0: "남성",
    "name": "철수",
    "age": 20,
}

print(x[0])
print(x["name"])
print("name" in x)
print(x.keys())
print(x.values())

for key in x:
    print("key: " + str(key))
    print("value: " + str(x[key]))

# value 변경
x[0] = "여성"
print(x)

# key: value 추가
x["job"] = "개발자"
print(x)