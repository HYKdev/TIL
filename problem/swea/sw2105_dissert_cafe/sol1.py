import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(start_i, start_j, start_value):
    q = deque()
    q.append([start_i, start_j, [start_value]])

    while q:
        i, j, q_sum = q.pop()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            while True:
                if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                    break

                if not visited[ni][nj] and matrix[ni][nj] not in q_sum:
                    q_sum.append(matrix[ni][nj])
                    q.append([ni, nj, q_sum])
                    visited[ni][nj] = 1

                elif matrix[ni][nj] in q_sum:
                    q_sum = []
                    break

                if ni == start_i and nj == start_j:
                    sum = 0
                    for alpa in q_sum:
                        sum += alpa
                    return sum

                ni += di[k]
                nj += dj[k]
    return -1


di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    ans = -1

    for i in range(1, n, 2):
        for j in range(1, n-1):
            visited = [[0 for _ in range(n)] for _ in range(n)]

            ans = BFS(i, j, matrix[i][j])
            # for a in visited:
            #     print(a)

    print(f'#{tc} {ans}')

