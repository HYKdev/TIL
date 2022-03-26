import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS():
    for _ in range(len(q)):
        i, j = q.popleft()

        ni = i + di[direction[i][j]]
        nj = j + dj[direction[i][j]]

        if 0 < ni < n-1 and 0 < nj < n-1:
            if not matrix[ni][nj]:
                matrix[ni][nj], matrix[i][j] = matrix[i][j], matrix[ni][nj]
                direction[ni][nj] = direction[i][j]
                direction[i][j] = -1

            elif matrix[ni][nj] and matrix[i][j] > max_matrix[ni][nj]:
                matrix[ni][nj] += matrix[i][j]
                matrix[i][j] -= matrix[ni][nj]
                direction[ni][nj] = direction[i][j]
                direction[i][j] = -1

            elif matrix[ni][nj] and matrix[i][j] < max_matrix[ni][nj]:
                matrix[ni][nj] += matrix[i][j]
                matrix[i][j] -= matrix[ni][nj]
                direction[i][j] = -1

        elif ni == 0 or ni == n-1 or nj == 0 or nj == n-1:
            matrix[ni][nj] = matrix[i][j]//2
            matrix[i][j] = 0
            direction[ni][nj] = direction_change(direction[i][j])
            direction[i][j] = -1

        if matrix[ni][nj]:
            q.append([ni, nj])

def direction_change(direc):
    if direc == 0:
        return 1
    elif direc == 1:
        return 0
    elif direc == 2:
        return 3
    elif direc == 3:
        return 2

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    direction = [[-1 for _ in range(n)] for _ in range(n)]
    max_matrix = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    for _ in range(k):
        r, c, micro, d = map(int, input().split())
        matrix[r][c] = micro
        direction[r][c] = d - 1
        q.append([r, c])

    for _ in range(m):
        BFS()

    total = 0
    for mat in matrix:
        total += sum(mat)

    print(f'#{tc} {total}')

