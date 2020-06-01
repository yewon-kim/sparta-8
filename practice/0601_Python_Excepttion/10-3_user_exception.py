class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한자리수 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자 : "))
    num2 = int(input("두 번째 숫자 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("오류 입력값: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("Value Error. 한자리수만 입력하세요.")
except BigNumberError as err:
    print("Big Number Error. 한자리수만 입력하세요.")
    print(err)

# finally
finally:
    print("계산기를 이용해 주셔서 감사합니다.")