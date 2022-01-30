# 최소공배수
T = int(input())

for _ in range(T):
    A , B = map(int,input().split())

    if A>B:
        R = A
    else:
        R = B
    for i in range(1, R+1):
        if A%i == 0 and B%i== 0:
            G = i
            a = A//i
            b = B//i
            
    print (G*a*b)