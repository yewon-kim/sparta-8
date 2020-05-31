# 자기소개를 하며 각자 다른 인사를 건네는 클래스를 짜보자

class Person:
    def __init__(self, name):
        self.name = name
    def meet(self, hello):
        print("내 이름은 {0}. {1}".format(self.name, hello))

waldo = Person("왈도")
waldo.meet("안녕하신가!")

class Police(Person):
    def arrest(self, hey):
        print("나는 {0} 경관이다. {1}".format(self.name, hey))

maxim = Police("막심")
maxim.meet("좋은 배짱이군.")
maxim.arrest("넌 체포됐다.")