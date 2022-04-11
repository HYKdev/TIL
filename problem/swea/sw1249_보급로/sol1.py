import sys
sys.stdin = open('input.txt')

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS(matrix, visited, time, S):
    q = deque()
    q.append(S)
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if ni == 0 and nj == 0:
                    continue
                elif not visited[ni][nj]:
                    visited[ni][nj] = True
                    time[ni][nj] = time[i][j] + matrix[ni][nj]
                    q.append([ni, nj])
                else:
                    if time[ni][nj] > time[i][j] + matrix[ni][nj]:
                        time[ni][nj] = time[i][j] + matrix[ni][nj]
                        q.append([ni, nj])


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    time = [[0 for _ in range(n)] for _ in range(n)]
    S = [0, 0]
    BFS(matrix, visited, time, S)
    ans = time[n - 1][n - 1]
    print(f'#{tc} {ans}')

