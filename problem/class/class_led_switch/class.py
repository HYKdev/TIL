import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    test = [0 for _ in range(n+1)]
    cnt = 0
    for i in range(1, n+1):
        if arr[i] != test[i]:
            j = i
            cnt += 1
            while j <= n:
                if test[j] == 1:
                    test[j] = 0
                else:
                    test[j] = 1
                j += i
    print(f'#{tc} {cnt}')

