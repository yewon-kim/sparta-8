fruits = ["사과", "딸기", "사과", "바나나", "바나나", "복숭아", "딸기", "사과", "키위"]
d = {}
for f in fruits:
    if f in d: 
        d[f] = d[f] + 1
    else:
        d[f] = 1
print(d)

responses = ["Like", "Wow", "Love", "Like", "Haha", "Wow", "Sad"]
result = {"Like": 0, "Love": 0, "Haha": 0, "Wow": 0, "Sad": 0, "Angry": 0}
for response in responses:
    if response in result:
        result[response] = result[response] + 1
    else:
        result[response] = 1
print(result)

courses = ["English", "Korean", "English", "Math", "Korean"]
likes = {}
for course in courses:
    if course in likes:
        likes[course] = likes[course] + 1
    else:
        likes[course] = 1
print(likes)