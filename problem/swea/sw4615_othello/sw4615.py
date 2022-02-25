import sys
import pprint
sys.stdin = open('input.txt')


T = int(input())
di = [0, 0, 1, 1, 1, -1, -1, -1]
dj = [1, -1, 0, 1, -1, 0, 1, -1]
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    matrix[n//2-1][n//2-1], matrix[n//2][n//2] = 2, 2
    matrix[n//2-1][n//2], matrix[n//2][n//2-1] = 1, 1

    for _ in range(m):
        i, j, color = map(int, input().split())
        i -= 1
        j -= 1
        matrix[i][j] = 1

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] != 0 and matrix[ni][nj] != color:
                while matrix[ni][nj] != color:
                    matrix[ni][nj] = color
                    ni = i + di[k]
                    nj = j + dj[k]

    pprint.pprint(matrix)
    print(f'#{tc} ')

