# Marine : 공격 유닛, 군인, 총을 쏠 수 있음
name_marine = "Marine"
hp_marine = 40
damage_marine = 5
print("{0} 유닛이 생성되었습니다.".format(name_marine))
print("체력: {0}\t공격력: {1}".format(hp_marine, damage_marine))

# Tank : 공격 유닛, 탱크, 포를 쏠 수 있음, 일반모드/시즈모드
name_tank = "Tank"
hp_tank = 150
damage_tank = 35
print("{0} 유닛이 생성되었습니다.".format(name_tank))
print("체력: {0}\t공격력: {1}".format(hp_tank, damage_tank))

# 공격 함수
def attack(name, location, damage):
    print("{0}\t{1} 방향으로 적을 공격합니다.\t[공격력: {2}]".format( \
        name, location, damage))

attack(name_marine, "1시", damage_marine)
attack(name_tank, "1시", damage_tank)