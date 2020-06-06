# global var 전역변수: 프로그램 전역에서 사용되는 var

item = 10
def stock(sold):
    global item
    item = item - sold
    print("재고: {0}개".format(item))

stock(0) # 현재 재고
stock(2) # 2개 팔림

# local var 지역변수: 호출된 함수 내에서만 사용되는 var

def stock_return(item):
    sold = input("판매량: ")
    item = int(item) - int(sold)
    print("남은 재고: {0}개".format(item))
    return item

item = input("현재 재고: ")
stock_return(item)