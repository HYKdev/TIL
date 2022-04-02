# 영역 구하기

import sys

sys.setrecursionlimit(100000)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
def dfs(i, j):
    global cnt
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and not matrix[ni][nj]:
            visited[ni][nj] = 1
            cnt += 1
            dfs(ni, nj)

m, n, k = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    c1, r1, c2, r2 = map(int, input().split())

    for r in range(r1, r2):
        for c in range(c1, c2):
            matrix[r][c] = 1

cnt_list = []
for r in range(m):
    for c in range(n):
        cnt = 1
        if not visited[r][c] and not matrix[r][c]:
            visited[r][c] = 1
            dfs(r, c)
            cnt_list.append(cnt)

cnt_list.sort()
print(len(cnt_list))
print(*cnt_list)