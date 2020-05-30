# parameter 매개변수 (ex. f(x, y)의 x, y)
# argument 인자(parameter에 대입된 값) (ex. f(3, 4)의 3, 4)

# 일반 함수
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름:{0}\t나이:{1}\t".format(name, age), end="\t")
    print(lang1, lang2, lang3, lang4, lang5)
profile("코난", 7, "영어", "일본어", "중국어", "한국어", "불어")
profile("미란", 16, "영어", "일본어", "", "", "")

# => para수만큼 arg를 넣어주어야 해서 불편하다!

### arbitrary argument(가변인자)를 사용한 함수
def profile(name, age, *langs):
    print("이름:{0}\t나이:{1}\t".format(name, age), end="\t")
    for lang in langs:
        print(lang, end=" ")
    print() # 줄바꿈

profile("코난", 7, "영어", "일본어", "중국어", "한국어", "불어", "스페인어")
profile("미란", 16, "영어", "일본어")

# => 인자의 수가 달라져도 된다!