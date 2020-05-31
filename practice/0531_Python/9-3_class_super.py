class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

### 다중상속 시에 super는 앞 class만 호출된다
#class FlyableUnit(Unit, Flyable):
#    def __init__(self):
#        super().__init__()

### 따라서 다중상속 시에는 각각 init을 해줘야 한다
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)
        
dropship = FlyableUnit()