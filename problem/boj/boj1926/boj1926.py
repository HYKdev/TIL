# 그림
# dfs로 풀면 메모리 초과 떠서 bfs로 풀어야 함

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dj = [0, 0, -1, 1]
di = [1, -1, 0, 0]
def dfs(i, j):
    global cnt
    matrix[i][j] = 0
    cnt += 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj]:
            dfs(ni, nj)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

cnt_list = []
for r in range(n):
    for c in range(m):
        if matrix[r][c] == 1:
            cnt = 0
            dfs(r, c)
            cnt_list.append(cnt)

if len(cnt_list) == 0:
    print(len(cnt_list))
    print(0)
else:
    print(len(cnt_list))
    print(max(cnt_list))