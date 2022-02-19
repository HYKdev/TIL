import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n = int(input())
# 50,000 10,000 5,000 1,000 500 100 50 10
    count = [0 for _ in range(8)]
    numbers = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    n = n//10*10

    i = 0
    while n > 0:
        if numbers[i] <= n:
            count[i] += 1
            n -= numbers[i]
        else:
            i += 1

    print(f'#{tc}')
    print(*count)

