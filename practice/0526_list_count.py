fruits = ["사과", "딸기", "사과", "바나나", "바나나", "복숭아", "딸기", "사과", "키위"]
d = {}
for f in fruits:
    if f in d: 
        d[f] = d[f] + 1
    else:
        d[f] = 1
print(d)