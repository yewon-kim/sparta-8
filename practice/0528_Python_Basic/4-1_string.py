hello = """
Hello there! 
Mighty fine morning, if you ask me! 
I'm Waldo.
"""
print(hello)

jumin = "960122-1234567"
print("성별: " + jumin[7]) # 7번 글자
print("출생년도: " + jumin[0:2]) # 0번 이상 2번 미만 글자들
print("출생일: " + jumin[4:6])
print("생년월일: " + jumin[:6]) # 처음부터 6번 미만까지
print("뒤 7자리: " + jumin[7:]) # 7번 이상 끝까지
print("뒤 7자리: " + jumin[-7:]) # 끝에서 7번째부터 역으로 끝까지