# inherit 상속

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}: {1} 방향으로 이동 [속도: {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AtkUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   # Unit의 __init__ 가져오기! 첫번째는 self!
        self.damage = damage

    def attack(self, location):
        print("{0}: {1} 방향으로 적을 공격합니다.\t[공격력: {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0}: {1}의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

firebat1 = AtkUnit("Firebat", 50, 3, 16)
firebat1.attack("5시")
firebat1.damaged(20)



### 다중 상속 Multiple Inherit ###

class FlyUnit:
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed

    def fly(self, name, location):
        print("{0}: {1} 방향으로 날아갑니다. [속도: {2}]"\
            .format(name, location, self.fly_speed))

class AtkFlyUnit(AtkUnit, FlyUnit):
    def __init__(self, name, hp, damage, fly_speed):
        AtkUnit.__init__(self, name, hp, 0, damage) # 지상 speed: 0
        FlyUnit.__init__(self, fly_speed)

    def move(self, location):   # move() 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

valkyrie = AtkFlyUnit("Valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


### 메소드 오버라이딩 Method Overiding ###

vulture = AtkUnit("Vulture", 80, 10, 20)
battlec = AtkFlyUnit("Battle Cruiser", 500, 25, 3)

vulture.move("11시")
battlec.move( "9시")


### pass ###
# 완성된 것처럼 보이게 하고 패스하는 것

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    pass
game_start()
game_over()


### super ###

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0) 혹은
        super().__init__(name, hp, 0)
        self.location = location

supply_depot = BuildingUnit("Supply Depot", 500, "7시")