# 아기 상어
from collections import deque

def BFS(args, args_size):
    time = 0
    fish = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append(args)
    visited[args[0]][args[1]] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if matrix[ni][nj] == 0 or matrix[ni][nj] == args_size:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i][j] + 1
                elif 1 <= matrix[ni][nj] < args_size:
                    visited[ni][nj] = visited[i][j] + 1
                    matrix[ni][nj] = 0
                    time = visited[ni][nj] - 1
                    
                    fish.append([ni, nj])
                    
    fish.sort()
    return fish

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
baby_shark = []

baby_shark_size = 2
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            baby_shark = [i, j]

fish_eat = 0
time = 0
print(BFS(baby_shark, baby_shark_size))
# while True:
#     fish = BFS(baby_shark, baby_shark_size)

#     if fish_eat // baby_shark_size == 1:
#         fish_eat = 0
#         baby_shark_size += 1

#     if fish:
#         break

# print(time)

