import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input())))
    rlt = 0

    for i in range(n//2):
        rlt += sum(arr[i][n//2-i: n//2+i+1])
        rlt += sum(arr[n-1-i][n//2-i: n//2+i+1])
    rlt += sum(arr[n//2])

    print(f'#{tc} {rlt}')

