# 주사위 게임

n = int(input())
a_cnt = 100
b_cnt = 100

for _ in range(n):
    a , b = map(int,input().split())


    if a == b:
        pass
    elif a > b:
        b_cnt -= a
    elif a < b:
        a_cnt -= b
    
print(a_cnt)
print(b_cnt)