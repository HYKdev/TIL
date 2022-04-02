# 단지번호붙이기

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def dfs(i, j):
    global cnt
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and matrix[ni][nj]:
            visited[ni][nj] = 1
            cnt += 1
            dfs(ni, nj)

n = int(input())
matrix = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

cnt_list = []
for r in range(n):
    for c in range(n):
        cnt = 1
        if not visited[r][c] and matrix[r][c]:
            visited[r][c] = 1
            dfs(r, c)
            cnt_list.append(cnt)

cnt_list.sort()
print(len(cnt_list))
for num in cnt_list:
    print(num)