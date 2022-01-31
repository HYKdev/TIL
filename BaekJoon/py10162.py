# 전자레인지

# A 300초 / B 60초 / C 10초

T = int(input())
cnt_A = 0
cnt_B = 0
cnt_C = 0

if T%10 != 0:
    print(-1)

while True:
    if T >= 300:
        cnt_A += 1
        T -= 300
    elif 300 > T >=60:
        cnt_B += 1
        T -= 60
    elif 60 > T > 0:
        cnt_C += 1
        T -= 10
    elif T == 0:
        print(cnt_A, cnt_B, cnt_C)
        break
    elif T%10 !=0:
        break
