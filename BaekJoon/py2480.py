dice_a, dice_b, dice_c = map(int,input().split())

if dice_a == dice_b == dice_c :
    print(10000+1000*dice_a)

elif (dice_a == dice_b) or (dice_a == dice_c):
    print(1000+100*dice_a)

elif dice_b == dice_c:
    print(1000+100*dice_b)

elif dice_a != dice_b != dice_c:
    if dice_a > dice_b and dice_a > dice_c:
        R = dice_a
    elif dice_b > dice_a and dice_b > dice_c:
        R = dice_b
    elif dice_c > dice_a and dice_c > dice_b:
        R =dice_c

    print(R*100)