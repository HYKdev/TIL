import sys
input = sys.stdin.readline

from collections import deque

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
def BFS(r, c):
    global move
    q = deque()
    q.append([r, c])
    total = matrix[r][c]
    country = [[r, c]]
    cnt = 1
    visited[r][c] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if L <= abs(matrix[ni][nj] - matrix[i][j]) <= R:
                    q.append([ni, nj])
                    visited[ni][nj] = 1
                    total += matrix[ni][nj]
                    country.append([ni, nj])
                    cnt += 1
                    move = True
    
    if move:
        for pos_i, pos_j in country:
            matrix[pos_i][pos_j] = total // cnt

n, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = 0 

while True:
    move = False
    visited = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                BFS(i, j)
    
    if move:
        answer += 1
    else:
        break

print(answer)