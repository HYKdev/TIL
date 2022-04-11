import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(s, e):
    q = deque()
    q.append(s)
    visited[s[0]][s[1]] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if not visited[ni][nj]:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i][j] + 1
                    if matrix[ni][nj] > matrix[i][j]:
                        visited[ni][nj] += (matrix[ni][nj] - matrix[i][j])
                elif visited[ni][nj] and matrix[ni][nj] >= matrix[i][j] and visited[ni][nj] > visited[i][j] + 1 + abs(matrix[ni][nj]-matrix[i][j]):
                    q.append([ni, nj])
                    visited[ni][nj] = (matrix[ni][nj]-matrix[i][j]) + visited[i][j] + 1
                elif visited[ni][nj] and matrix[ni][nj] < matrix[i][j] and visited[ni][nj] > visited[i][j] + 1:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])

    return visited[e[0]][e[1]]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    start, end = [0, 0], [n-1, n-1]


    print(f'#{tc} {BFS(start, end)-1}')

