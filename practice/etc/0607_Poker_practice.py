import random

### 게임 준비 ###
# shapes/nums 정의
# ♣♥♦♠
shapes = [i for i in range(1, 4)]
# 2345678910JQKA
nums = [i for i in range(2, 15)]

# 덱 만들기
deck = []
for shape in shapes:
    for num in nums:
        deck.append((shape, num))
random.shuffle(deck)

# 플레이어에게 카드 나누기
player = []
computer = []

for i in range(5):
    player.append(deck.pop())
    computer.append(deck.pop())

def CardRank(cards):
    # 페어 확인
    paircount = 0
    for i in range(0, 4):
        for j in range(i + 1, 5):
            if cards[i][1] == cards[j][1] :
                paircount = paircount + 1
    
    # 스트레이트 확인
    num = [cards[i][1] for i in range(5)]
    num.sort()
    straight = False
    if paircount == 0:
        if (num[4] - num[0]) == 4:
            straight = True
        if num[0] == 2 and num[1] == 3 and num[2] == 4 and num[3] == 5 and num[4] == 14:
            straight = True
        if num[0] == 2 and num[1] == 3 and num[2] == 4 and num[3] == 13 and num[4] == 14:
            straight = True
        if num[0] == 2 and num[1] == 3 and num[2] == 12 and num[3] == 13 and num[4] == 14:
            straight = True
        if num[0] == 2 and num[1] == 11 and num[2] == 12 and num[3] == 13 and num[4] == 14:
            straight = True
    
    # 플러시 확인
    shape = [cards[i][0] for i in range(5)]
    shape.sort()
    flush = False
    if shape[0] == shape[4]:
        flush = True
    
    # 최종 랭크
    if straight and flush: # 스트레이트 플러시
        rank = 1
    elif paircount == 6: # 포카드
        rank = 2
    elif paircount == 4: # 풀하우스
        rank = 3
    elif flush: # 플러시
        rank = 4
    elif straight: # 스트레이트
        rank = 5
    elif paircount == 3: # 트리플
        rank = 6
    elif paircount == 2: # 투페어
        rank = 7
    elif paircount == 1: # 원페어
        rank = 8
    else: # 노페어
        rank = 9
    return rank

def ranking(rank):
    if rank == 1:
        return '스트레이트 플러시'
    if rank == 2:
        return '포카드'
    if rank == 3:
        return '풀하우스'
    if rank == 4:
        return '플러시'
    if rank == 5:
        return '스트레이트'
    if rank == 6:
        return '트리플'
    if rank == 7:
        return '투페어'
    if rank == 8:
        return '원페어'
    if rank == 9:
        return '노페어'

rank_player = CardRank(player)

print('나의 카드:', player, '\n나의 랭크:', ranking(rank_player))

while True:
    if len(player) == 0:
        break
    i = int(input("\n몇 번째 카드를 버리시겠습니까? (0: 종료) >>> "))
    if i == 0:
        break
    else:
        selected = player[i - 1]
        player.remove(selected)
        print('나의 카드:', player)

get = 5 - len(player)
print('\n덱에서 카드 {0}장을 가져옵니다.\n'.format(get))
for i in range(0, get):
    player.append(deck.pop())

print('나의 카드:', player, '\n나의 랭크:', ranking(rank_player))

rank_com1 = CardRank(computer)
print('상대 카드:', computer, '\n상대 랭크:', ranking(rank_com1))

print('')

if CardRank(player) > CardRank(computer):
    print("플레이어 승!")
elif CardRank(player) < CardRank(computer):
    print("컴퓨터 승!")
else:
    print("무승부!")