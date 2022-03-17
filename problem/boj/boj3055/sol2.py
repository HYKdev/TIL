from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(input().strip()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

q = deque()

def bfs():
    while q:
        i, j = q.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < r and 0 <= nj < c:
                if graph[ni][nj] == 'D' and graph[i][j] == 'S':
                    return visited[i][j] + 1
                elif graph[ni][nj] == '.' and graph[i][j] == 'S':
                    graph[ni][nj] = 'S'
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])
                elif (graph[ni][nj] == '.' or graph[ni][nj] == 'S') and graph[i][j] == '*':
                    graph[ni][nj] = '*'
                    q.append([ni, nj])

    return "KAKTUS"

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            q.append([i, j])

for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            q.append([i, j])

print(bfs())

# 체크용
# for a in graph:
#     print(a)
# print('------graph-------')
# for b in visited:
#     print(b)
# print('------visited------')