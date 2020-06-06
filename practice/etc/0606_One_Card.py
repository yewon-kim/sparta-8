import random

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
print(deck)
random.shuffle(deck)
print(deck)

# 플레이어에게 카드 나누기

player = []
computer = []

for i in range(7):
    player.append(deck.pop())
    computer.append(deck.pop())

# 낸 카드에 하나 올려놓기
put = []
put.append(deck.pop())

# 게임 시작
while True:

    # 플레이어 턴
    # 카드를 내거나 먹음

    if len(player) == 0:
        print("플레이어가 이겼습니다!")
        break

    # 컴퓨터 턴
    # 카드를 내거나 먹음

    if len(computer) == 0:
        print("컴퓨터가 이겼습니다!")
        break