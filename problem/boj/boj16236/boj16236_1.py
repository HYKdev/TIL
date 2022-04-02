import sys

input = sys.stdin.readline
from collections import deque

def BFS():
    global total_time, baby_shark, matrix
    
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append([baby_shark['position'][0], baby_shark['position'][1], 0])
    visited[baby_shark['position'][0]][baby_shark['position'][1]] = 1

    min_time = float('inf')
    fish_eat_list = []
    while q:
        i, j, time = q.popleft()
        
        print(i, j, time)
        for a in visited:
            print(a)
        print('---------')
        for b in matrix:
            print(b)
        print(baby_shark)
        
        if time > min_time:
            break

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if 0 <= matrix[ni][nj] <= baby_shark['size']:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj, visited[ni][nj]])
                    print(q)
                    if 0 < matrix[ni][nj] < baby_shark['size']:
                        if min_time >= visited[ni][ni]:
                            min_time = visited[ni][nj]
                            fish_eat_list.append([ni, nj])
    fish_eat_list.sort()

    if not fish_eat_list:
        print(total_time)
        exit(0)
    else:
        matrix[baby_shark['position'][0]][baby_shark['position'][1]] = 0
        baby_shark['position'] = fish_eat_list[0]
        total_time += min_time

        matrix[fish_eat_list[0][0]][fish_eat_list[0][1]] = 9
        baby_shark['eat_fish'] += 1
        
        if baby_shark['eat_fish'] == baby_shark['size']:
            baby_shark['eat_fish'] = 0
            baby_shark['size'] += 1

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
total_time = 0
baby_shark = {
    'position' : [0, 0],
    'size' : 2,
    'eat_fish' : 0,
}

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            baby_shark['position'] = [i, j]

while True:
    BFS()
