# class
# __init__: 첫 인자로 self

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력: {0}\t공격력: {1}".format(self.hp, self.damage))

# 객체 생성: self를 제외한 나머지 arg 대입
marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank = Unit("Tank", 150, 35)

# self 부분에 객체명 넣어서 호출 가능
wraith1 = Unit("Wraith", 80, 5)
print("유닛명: {0}\t공격력: {1}".format(wraith1.name, wraith1.damage))

# 변수 추가 할당
wraith2 = Unit("Wraith", 80, 5)
wraith2.clocking = True
if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


### METHOD ###
class AttackUnit():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    # 공격
    def attack(self, location):
        print("{0}: {1} 방향으로 적을 공격합니다. [공격력: {2}]"\
            .format(self.name, location, self.damage))
    # 피해
    def damaged(self, damage):
        print("{0}: {1}의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

# Firebat
firebat1 = AttackUnit("Firebat", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)