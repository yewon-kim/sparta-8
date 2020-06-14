# 369 게임
def threeSixNine(n):
    list = []
    for i in range(1, n + 1):
        count_three = str(i).count('3')
        count_six = str(i).count('6')
        count_nine = str(i).count('9')
        count_clap = count_three + count_six + count_nine
        if count_clap == 0:
            list.append(i)
        else:
            clap = '짝' * count_clap
            list.append(clap)
    return list

for i in range(33):
    print(threeSixNine(33)[i])

# FizzBuzz : 3의 배수는 Fizz, 5의 배수는 Buzz, 3과 5의 공배수는 FizzBuzz 표시
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)  

for i in range(1, 16):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)