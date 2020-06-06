import random
mymoney = 10000
while 1:
    print("주사위 게임 Ver 1.0")
    print(" 1. GAME START")
    print(" 0. GAME EXIT")
    
    sel = int(input(" >"))

    if sel == 0:
        print("=== GAME EXIT ===")
        break
    elif sel == 1:
        print("=== GAME START ===")
        com = ply = 0
        bet = 10
        for x in range(3):
            com += random.randrange(1,7)
            ply += random.randrange(1,7)

        print("DICE SUM : ", ply)
        if(input("BET MONEY (y. yes) ? ") == "y"):
            tmp = int(input("$20~$%d : "%mymoney))
            if tmp > mymoney or tmp < 20:
                print("ERR : Out of range...")
            else :
                bet += tmp

        print("")
        if ply > com :
            print("Victory!!")
            mymoney += bet
        elif ply < com :
            print("Lose...")
            mymoney -= bet
        else :
            print("Draw...")

        print("\n=== You Have : $%d ===\n\n"%mymoney)