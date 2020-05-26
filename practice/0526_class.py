class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, feeling):
        print(feeling + " 아침! " + "만일 내게 묻는다면 나는 " + self.name + ". " + str(self.age) + "살.")

waldo = Person("왈도", 20)

waldo.say_hello("힘세고 강한")