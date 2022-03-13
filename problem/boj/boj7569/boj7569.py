# 토마토

import sys
from collections import deque

M, N, H = map(int, input().split())
dm = [0, 0, 1, -1, 0, 0]
dn = [1, -1, 0, 0 ,0 ,0]
dh = [0, 0, 0, 0, 1, -1]
tomato = []
matrix = [[] for _ in range(H)]
for k in range(H):
    for i in range(N):
        matrix[k].append(list(map(int, input().split())))
        for j in range(M):
            if matrix[k][i][j] == 1:
                tomato.append([k,i,j])


def BFS():

    q= deque()
    for point in tomato:
        q.append(point)
    cnt = -1

    while q:
        h,n,m = q.popleft()
        for l in range(6):
            nm = m + dm[l]
            nn = n + dn[l]
            nh = h + dh[l]
            if 0 <= nn < N and 0 <= nm < M and 0 <= nh < H and matrix[nh][nn][nm]== 0:
                q.append([nh,nn,nm])
                matrix[nh][nn][nm] += matrix[h][n][m] + 1
    
        cnt = matrix[h][n][m] -1

    for z in matrix:
        for x in z:
            if 0 in x:
                return -1
    return cnt

print(BFS())