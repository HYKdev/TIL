import sys

sys.stdin = open('input.txt')

di_1 = [0, 0, 1, -1]
dj_1 = [1, -1, 0, 0]
di_2 = [1, 1, -1, -1]
dj_2 = [1, -1, 1, -1]

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    max_attack = 0
    for i in range(n):
        for j in range(n):
            each_attack_1 = matrix[i][j]
            each_attack_2 = matrix[i][j]
            for d in range(1, m):
                for k in range(4):
                    ni_1 = i + di_1[k] * d
                    nj_1 = j + dj_1[k] * d
                    ni_2 = i + di_2[k] * d
                    nj_2 = j + dj_2[k] * d
                    if 0 <= ni_1 < n and 0 <= nj_1 < n:
                        each_attack_1 += matrix[ni_1][nj_1]
                    if 0 <= ni_2 < n and 0 <= nj_2 < n:
                        each_attack_2 += matrix[ni_2][nj_2]
            max_attack = max(each_attack_1, each_attack_2, max_attack)

    print(f'#{tc} {max_attack}')

