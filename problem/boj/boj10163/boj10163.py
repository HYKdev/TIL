import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = [[0 for _ in range(1001)] for _ in range(1001)]
    n = int(input())
    max_r = 0
    max_c = 0
    for k in range(n):
        x, y, r, c = map(int, input().split())
        if max_r < r:
            max_r = r

        if max_c < c:
            max_c = c

        for i in range(x, r):
            for j in range(y, c):
                arr[i][j] = k

    for i in range(max_r):
        for j in range(max_c):




    print(f'#{tc} ')

