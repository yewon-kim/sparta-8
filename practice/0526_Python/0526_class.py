class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, feeling):
        print(feeling + " 아침! " + "만일 내게 묻는다면, 나는 " + self.name + ". " + str(self.age) + "살.")

waldo = Person("왈도", 20)

waldo.say_hello("힘세고 강한")

class Police(Person):
    def arrest(self, to_arrest):
        print("안녕하신가! 나는 " + self.name + ". 넌 체포됐다, " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("난 " + self.name + ". 개발한다, " + to_program)

john = Person("존", 17)
jane = Police("제인", 21)
alex = Programmer("알렉스", 25)

john.say_hello("좋다")
jane.arrest("왈도")
alex.program("급식앱")