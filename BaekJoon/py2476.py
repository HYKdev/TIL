# 주사위 게임

N = int(input())
R1 = 0
for i in range(N):
    a,b,c = map(int,input().split())

    N_list = sorted([a,b,c])

    if N_list[0] == N_list[2]:
        R1 = max(R1, 10000+1000*N_list[0])
    elif N_list[0] == N_list[1] or N_list[1] == N_list[2]:
        R1 = max(R1, 1000+100*N_list[1])
    elif N_list[0] != N_list[1] != N_list[2]:
        R1 = max(R1, 100*N_list[2])
print(R1)