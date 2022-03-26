#토마토

from collections import deque
import sys

def BFS():
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if matrix[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    matrix[ni][nj] = 1
                    q.append([ni, nj])

def ans_test():
    ans = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                ans = -1
                return ans
            elif visited[i][j]:
                ans = max(ans, visited[i][j])
    ans -= 1
    return ans

input = sys.stdin.readline

m, n = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
q = deque()
di = [0, 0, -1 ,1]
dj = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.append([i, j])
            visited[i][j] = 1

BFS()

print(ans_test())