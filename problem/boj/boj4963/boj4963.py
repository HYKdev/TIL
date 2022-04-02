# 섬의 개수

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

di = [0, 0, 1, 1, 1, -1, -1, -1]
dj = [1, -1, 0, 1, -1, 0, 1, -1]

def DFS(ii, jj):
    for k in range(8):
        ni = ii + di[k]
        nj = jj + dj[k]
        if 0 <= ni < r and 0 <= nj < c and matrix[ni][nj]:
            matrix[ni][nj] = 0
            DFS(ni, nj)

while True:
    c, r = map(int, input().split())

    if c == 0 and r == 0:
        break

    matrix = [list(map(int, input().split())) for _ in range(r)]
    island = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j]:
                matrix[i][j] = 0
                DFS(i, j)
                island += 1
    
    print(island)