# 분산 처리기

T = int(input())

ans_2 = [6, 2, 4, 8]
ans_3 = [1, 3, 9, 7]
ans_4 = [6, 4]
ans_7 = [1, 7, 9, 3]
ans_8 = [6, 8, 4, 2]
ans_9 = [1, 9]
for _ in range(T):
    a, b = map(int, input().split())

    if a%10 == 1:
        print(1)
    elif a%10 == 2:
        print(ans_2[b%4])
    elif a%10 == 3:
        print(ans_3[b%4])
    elif a%10 == 4:
        print(ans_4[b%2])
    elif a%10 == 5:
        print(5)
    elif a%10 == 6:
        print(6)
    elif a%10 == 7:
        print(ans_7[b%4])
    elif a%10 == 8:
        print(ans_8[b%4])
    elif a%10 == 9:
        print(ans_9[b%2])
    elif a%10 == 0:
        print(10)
