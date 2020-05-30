# return 값이 없는 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

# return 값이 있는 함수
def deposit(balance, money): # 입금
    print("입금 완료 | 잔액: {0}원".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance > money: # 잔액 > 출금액
        print("출금 완료 | 잔액: {0}원".format(balance - money))
    else:
        print("잔액이 모자랍니다. | 잔액: {0}원".format(balance))
    return balance - money

balance = 0 # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)