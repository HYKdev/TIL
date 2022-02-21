import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = [[0 for _ in range(1001)] for _ in range(1001)]
    n = int(input())

    for k in range(1, n+1):
        x, y, c, r = map(int, input().split())
        for i in range(y, y+r):
            arr[i][x:x+c] = [k]*c

    for j in range(1, n+1):
        result = 0
        for cnt in range(1001):
            result += arr[cnt].count(j)
        print(result)