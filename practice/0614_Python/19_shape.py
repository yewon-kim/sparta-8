# 삼각형
for i in range(5):
    for j in range(5):
        if j <= i:
            print("*", end=" ")
    print("")

# 삼각형 - 상하반전
for i in range(5):
    for j in range(5):
        if j >= i:
            print("*", end=" ")
    print("")

# 삼각형 - 좌우반전
for i in range(5):
    for j in range(5):
        if j < 4 - i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print("")

# 삼각형 - 상하좌우반전
for i in range(5):
    for j in range(5):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")

# 정사각형 테두리
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4:
            print("*", end=" ")
        elif j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")

# 체크무늬
for i in range(5):
    for j in range(5):
        if i % 2 == 0:
            if j % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            if j % 2 == 0:
                print(" ", end=" ")
            else:
                print("*", end=" ")
    print("")