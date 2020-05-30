# 01. 삼각형 넓이 구하는 함수
def f(w, h):
    y = (1/2) * w * h
    print(y)
    return(y)
f(20, 10)

# 02. 문제 한 번 내는 함수
def exam_once(question, answer):
    reply = input(question)
    if reply == answer:
        print("정답입니다!")
    else:
        print("오답입니다.")
exam_once("1 + 1 = ", "2")

# 03. 문제 계속 내는 함수
def exam_while(question, answer):
    reply = ""
    while reply != answer:
        reply = input(question)
        if reply == answer:
            print("당신은 훌륭한 아재입니다.")
        elif reply == "hint":
            print("hint: 대학이 3월에 무엇을 하는지 생각해 보세요.")
        else:
            print("다시 생각해 보세요.")

exam_while(
    "대학생들이 3월에 강한 이유는? ",
    "개강해서"
)