# 임시 반장 정하기

#


N = int(input())
N_list = []
for _ in range(N):
    x1, x2, x3, x4, x5 = map(int,input().split())
    N_list.append([x1, x2, x3, x4, x5])
N_lists = []
for i in range(5):
    for j in range(N):
        N_lists.extend(N_list[j][i])