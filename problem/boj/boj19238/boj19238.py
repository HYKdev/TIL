#스타트 택시

from collections import deque

size, passenger, energe = map(int, input().split())
matrix = []
for i in range(size):
    matrix.append(list(int, input().split()))
    for j in range(size):
        if matrix[i][j] == 1:
            matrix[i][j] = -1

a,b = list(map(int, input().split()))
taxi_position = [a-1, b-1]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
passenger_start = []
passenger_end = []
for _ in range(passenger):
    r1, c1, r2, c2 = map(int, input().split())

    passenger_start.append([r1-1,c1-1])
    passenger_end.append([r2-1,c2-1])


def BFS(position_start, position_end):
    q = deque()
    q.append(position_start)
    visited = [[False]*size for _ in range(size)]
    visited[position_start[0]][position_start[1]] = True
    cnt = 0

    while q:
        i, j = q.popleft()
        if [i,j] in position_end:
            result = [i,j,cnt]
            return result
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < size and 0 <= nj < size and not visited[ni][nj] and matrix[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni,nj])
                matrix[ni][nj] += matrix[i][j] + 1
        cnt = matrix[i][j]


print(BFS(taxi_position, passenger_start))