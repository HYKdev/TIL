import sys

sys.stdin = open('input.txt')

def sum_fly(r1, c1):
    sum = 0
    for i in range(m):
        for j in range(m):
            sum += data[r1 + i][c1 + j]
    return sum
T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    max_sum = 0

    for x in range(n-m+1):
        for y in range(n-m+1):
            if max_sum < sum_fly(x, y):
                max_sum = sum_fly(x, y)

    print(f'#{tc} {max_sum}')

