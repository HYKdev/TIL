# 안전영역

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def dfs(i, j, high):
    
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<= ni < n and 0 <= nj < n and not visited[ni][nj] and matrix[ni][nj] > high:
            visited[ni][nj] = 1
            dfs(ni, nj, high)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_high = max(map(max, matrix))
min_high = min(map(min, matrix))
ans = 1

for k in range(min_high, max_high):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > k and not visited[i][j]:
                visited[i][j] = 1
                dfs(i, j, k)
                cnt += 1
    ans = max(cnt, ans)

print(ans)