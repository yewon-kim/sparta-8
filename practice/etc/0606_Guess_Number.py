from random import *

print('안녕하신가. 당신의 이름은?')
name = input("> ")
print('반갑네, {0}!'.format(name))
while True:
    number = randrange(1, 20)
    print('나는 1 ~ 20 중 한 숫자를 생각하고 있다네.')
    print('한번 맞춰보게.')
    i = 1
    while True:
        guess = int(input("> "))
        if guess > number:
            print('너무 크다네. 다시 생각해 보게.')
            i += 1
        elif guess < number:
            print('너무 작다네. 다시 생각해 보게.')
            i += 1
        else:
            print('정답이네, {0}! {1}번만에 맞췄어.'.format(name, i))
            break
    print('\n>>> 다시 시작하시겠습니까?(y/n) <<<')
    reply = input("> ")
    if reply == 'y':
        print('좋아. 다시 해 보지.')
    elif reply == 'n':
        print('다음에 또 보자고, {0}.'.format(name))
        break