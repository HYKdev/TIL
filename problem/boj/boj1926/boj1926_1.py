# 그림

import sys
from collections import deque
input = sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def BFS(r, c):
    q = deque()
    q.append([r, c])
    matrix[r][c] = 0
    cnt = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj]:
                matrix[ni][nj] = 0
                cnt += 1
                q.append([ni, nj])
    return cnt
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

ans_lst = []
for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            result = BFS(i, j)
            ans_lst.append(result)

if len(ans_lst) == 0:
    print(0)
    print(0)
else:
    print(len(ans_lst))
    print(max(ans_lst))