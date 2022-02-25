import sys

sys.stdin = open('input.txt')

T = int(input())

di_1 = [0, 0, 1, -1]
dj_1 = [1, -1, 0, 0]
di_2 = [1, 1, -1, -1]
dj_2 = [-1, 1, -1, 1]
for tc in range(1, T+1):
    n, p = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    max_total = 0
    for i in range(n):
        for j in range(n):
            total_1 = matrix[i][j]
            total_2 = matrix[i][j]
            for a in range(1, p+1):
                for k in range(4):
                    ni_1 = i + di_1[k] * a
                    nj_1 = j + dj_1[k] * a
                    ni_2 = i + di_2[k] * a
                    nj_2 = j + dj_2[k] * a
                    if 0 <= ni_1 < n and 0 <= nj_1 < n:
                        total_1 += matrix[ni_1][nj_1]
                    if 0 <= ni_2 < n and 0 <= nj_2 < n:
                        total_2 += matrix[ni_2][nj_2]
            max_total = max(max_total, total_1, total_2)

    print(f'#{tc} {max_total}')
