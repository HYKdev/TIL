# 유기농 배추

from collections import deque
import sys

input = sys.stdin.readline

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def BFS():
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 1:
                matrix[ni][nj] = 0
                q.append([ni, nj])


T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())

    matrix = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    
    for _ in range(k):
        c, r = map(int, input().split())
        matrix[r][c] = 1


    cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                q.append([i, j])
                BFS()
                cnt += 1


    print(cnt)
 