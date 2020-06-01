def stock(item):
    print("[재고: {0}]".format(item))
    class SoldOutError(Exception):
        pass

    number = 1
    while item != 0:
        try:
            order = int(input("주문 수량: "))
            if item < order:
                print("주문 수량이 재고를 초과했습니다.")
            elif order <= 0:
                raise ValueError
            else:
                print("[주문번호: {0}] {1}개 주문 완료".format(number, order))
                number += 1
                item -= order
                print("[재고: {0}]".format(item))

            if item == 0:
                raise SoldOutError

        except ValueError:
            print("주문 수량은 0보다 커야 합니다.")
        except SoldOutError:
            print("매진되었습니다.")
            break
stock(100)