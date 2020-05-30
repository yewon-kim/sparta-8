# 파일 입출력 / 불러오기, 열기

# open("파일명.확장자", "r(읽기)|w(쓰기)|a(추가)")

# w(쓰기) : 파일 존재 시 내용 덮어쓰기, 없었다면 파일 생성

score_file = open("score.txt", "w", encoding="utf8")
print("Math: 80", file=score_file)
print("English: 50", file=score_file)
score_file.close()

# a(추가) : 파일 마지막 부분에 추가

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("Science: 75\n")
score_file.write("Programming: 100")
score_file.close()

# r(읽기) : 파일 내용 읽어오기
# read() : 전체 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# readline() : 한 줄 읽고 커서는 다음 줄로 이동
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()