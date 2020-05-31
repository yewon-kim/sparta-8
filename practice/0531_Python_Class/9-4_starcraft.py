from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]", end=" ")
        print("{0}: {1} 방향으로 이동 [속도: {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0}: {1}의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

# 공격 유닛
class AtkUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   # Unit의 __init__ 가져오기! 첫번째는 self!
        self.damage = damage

    def attack(self, location):
        print("{0}: {1} 방향으로 적을 공격합니다.\t[공격력: {2}]"\
            .format(self.name, location, self.damage))

# 마린
class Marine(AtkUnit):
    def __init__(self):
        AtkUnit.__init__(self, "마린", 40, 1, 5)
    
    # 스팀팩 : 일정 시간 이동/공격 속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0}: 스팀팩을 사용합니다. [HP 10 감소]".format(self.name))
        else:
            print("{0}: 체력 부족. 스팀팩 사용 불가.".format(self.name))

# 탱크
class Tank(AtkUnit):
    # 시즈모드 : 전 탱크 지상 고정, 공격력 상승, 이동 불가
    seize_developed = False

    def __init__(self):
        AtkUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return    
        # 일반모드 -> 시즈모드
        if self.seize_mode == False:
            print("{0}: 시즈모드 발동.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 시즈모드 -> 해제
        else:
            print("{0}: 시즈모드 해제.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


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
        print("[공중 유닛 이동]", end=" ")
        self.fly(self.name, location)

# 레이스
class Wraith(AtkFlyUnit):
    def __init__(self):
        AtkFlyUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드: 해제 상태

    def clocking(self):
        if self.clocked == True:
            print("{0}: 클로킹 모드 해제.".format(self.name))
            self.clocked == False
        else:
            print("{0}: 클로킹 모드 발동.".format(self.name))
            self.clocked == True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    print("Player: gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


### 실제 게임 진행 ###

game_start()

# 유닛 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발 완료.")

# 공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹 모드)
for unit in attack_units:
    if isinstance(unit, Marine): # 어떤 class의 instance인지 확인
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))

# 게임 종료
game_over()