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
    print(list)

threeSixNine(33)