# Yangjojang of The Year

T = int(input())

S_list = []
L_list = []
for _ in range(T):
    N = int(input())
    for _ in range(N):
        S, L = input().split()
        L = int(L)

        S_list.append(S)
        L_list.append(L)
    
    for i in range(N):
        if L_list[i] == max(L_list):
            print(S_list[i])
