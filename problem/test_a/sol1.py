import sys
sys.stdin = open('input1.txt')

from collections import deque

def BFS(i, j, d_m):
    global max_total
    q =deque()
    q.append([i, j])
    visited_1[i][j] = [1, matrix[i][j]]
    d_m[i][j] = 0
    while q:
        ii, jj = q.popleft()
        for a in visited_1:
            print(a)
        print('-------------')
        for k in range(4):
            ni = ii + di[k]
            nj = jj + dj[k]
            if 0 <= ni < r and 0 <= nj < c:
                if not visited_1[ni][nj]:
                    visited_1[ni][nj] = [visited_1[ii][jj][0] + 1, visited_1[ii][jj][1] + d_m[ni][nj]]
                    d_m[ni][nj] = 0
                    if visited_1[ni][nj][0] == 4:
                        max_total = max(max_total, visited_1[ni][nj][1])
                    elif visited_1[ni][nj][0] < 4:
                        q.append([ni, nj])

                # elif visited_1[ni][nj]:
                #     if visited_1[ni][nj][1] < visited_1[ii][jj][1] + matrix[ni][nj]:
                #         visited_1[ni][nj] = [visited_1[ii][jj][0] + 1, visited_1[ii][jj][1] + matrix[ni][nj]]
                #
                #         if visited_1[ni][nj][0] == 4:
                #             max_total = max(max_total, visited_1[ni][nj][1])
                #         elif visited_1[ni][nj][0] < 4:
                #             q.append([ni, nj])


def DFS(cnt, total):


di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
T = int(input())
for tc in range(1, T + 1):
    c, r = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(r)]

    max_total = 0

    for i in range(r):
        for j in range(c):
            visited_1 = [[[] for _ in range(c)] for _ in range(r)]
            deep_matrix = [mat[:] for mat in matrix]
            BFS(i, j, deep_matrix)

    print(f'#{tc} {max_total**2}')

