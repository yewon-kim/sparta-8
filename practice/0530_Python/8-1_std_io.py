### STANDARD OUTPUT 표준 출력 ###

# separate로 구분 설정
print("Python", "Java", sep=", ")
print("Python", "Java", sep=" vs ")

# end 변경으로 한 줄 내 표현
print("Python", "Java", sep=" vs ", end=" 세기의 대결\n")

# file = sys.stdout
import sys # sys 모듈
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러

# dictionary 출력 시 정렬
# .ljust(n) : 왼쪽부터 n칸의 공간 생성 후 정렬
# .rjust(n) : 오른쪽부터 n칸의 공간 생성 후 정렬

scores = {"Math": 65, "Science": 80, "Programming": 50}
for subject, score in scores.items():
    print(subject.ljust(12), str(score).rjust(4), sep=":")

# zfill(n) : str의 n칸을 0으로 채움

for num in range(1, 11):
    print("대기번호", str(num).zfill(3), sep=" : ")


### STANDARD INPUT 표준 입력 ###

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 ", answer, "입니다.", sep="")

# 사용자 input은 항상 str으로 받는다는 점에 유의!