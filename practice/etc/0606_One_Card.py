import random

### 게임 준비 ###
# num과 shape 정의
shapes = '♥♣♠♦'
nums = []
for i in range(2,11):
    nums.append(str(i))
for c in 'JQKA':
    nums.append(c)

# 덱 만들기
deck = []
print(deck)
for shape in shapes:
    for num in nums:
        deck.append((shape, num))

deck.append(('Joker', 'black'))
deck.append(('Joker', 'colored'))

random.shuffle(deck)

# 플레이어에게 카드 나누기
player = []
computer = []

for i in range(7):
    player.append(deck.pop())
    computer.append(deck.pop())

# 낸 카드에 하나 올려놓기
put = []
put.append(deck.pop())

# 낼 수 있는 카드 리스트
def getAvailable(hand, last_card):
    available = []
    for card in hand:
        if (card[0] == last_card[0]
            or card[1] == last_card[1]
            or card[0] == 'Joker'
            or put[-1][0] == 'Joker'):
            available.append(card)
    return available

# 턴


### 게임 시작 ###
while True:

    # 플레이어 턴
    print("\n플레이어의 차례입니다.")
    print("현재 패 >>", player)
    print("놓인 카드 >>", put[-1]) # [-1]은 마지막 카드

    # 가능한 카드 출력
    available = getAvailable(player, put[-1])

    print("낼 수 있는 카드: ", available)

    if len(available) > 0:
        i = int(input("몇 번째 카드를 내시겠습니까? >>> "))
        i -= 1
        selected = available[i]
        player.remove(selected)
        put.append(selected)
    else:
        print("낼 수 있는 카드가 없어 1장을 먹습니다.")
        player.append(deck.pop())

    if len(player) == 0:
        print("플레이어가 이겼습니다!")
        # break

    # 컴퓨터 턴
    print("\n컴퓨터의 차례입니다.")
    print("놓인 카드 >>", put[-1])

    # 가능한 카드
    available = getAvailable(computer, put[-1])

    if len(available) > 0:
        selected = random.choice(available)
        computer.remove(selected)
        put.append(selected)
        print("컴퓨터가 {0}을 냈습니다.".format(selected))
    else:
        print("낼 수 있는 카드가 없어 1장을 먹습니다.")
        computer.append(deck.pop())

    if len(computer) == 0:
        print("컴퓨터가 이겼습니다!")
        # break