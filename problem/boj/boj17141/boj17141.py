# 연구소2

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def BFS(list):
    q = deque()
    cnt = 1
    for lst in list:
        q.append(lst)
    while q:
        [i, j] = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if matrix[ni][nj] == 0 or matrix[ni][nj] == 2:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

virus_position_list = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            virus_position_list.append([i, j])

min_time = n * n
time_list = []
for lst in combinations(virus_position_list, m):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    point_list =[]
    for point in lst:
        point_list.append(point)
        visited[point[0]][point[1]]

    BFS(point_list)
    time = 0
    for i in range(n):
        for j in range(n):
            if time < visited[i][j]:
                time = visited[i][j]
            
            if visited[i][j] == 0 and matrix[i][j] != 1:
                time = -1
                break

    time_list.append(time)
    

print(time_list)