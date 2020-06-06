user = "남양주 소방서"
i = 3
while 0 < i:
    print("{0}입니다. {1}초 남았습니다.".format(user, i))
    i -= 1

print("경기도지삽니다.")

user = "관등성명"
person = "unknown"
while person != user:
    person = input("거 이름이 누구요? ")
    if person == user:
        print("어, 그래. 끊어요.")
    else:
        print("{0}을 대야지.".format(user))

right = "개강해서"
answer = ""
while answer != right:
    answer = input("대학생들이 3월에 강한 이유는? ")
    if answer == right:
        print("당신은 훌륭한 아재입니다.")
    else:
        print("hint: 대학이 3월에 무엇을 하는지 생각해 보세요.")