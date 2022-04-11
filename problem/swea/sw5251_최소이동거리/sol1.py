import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    n, e = map(int, input().split())
    INF = float('inf')
    visited = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(e):
        a, b, w = map(int, input().split())

        visited[a][b] = w

    dp = [INF] * (n+1)
    dp[0] = 0

    for i in range(n+1):
        for j in range(n+1):
            if dp[i] + visited[i][j] < dp[j]:
                dp[j] = dp[i] + visited[i][j]

    print(dp)
    print(visited)
    answer = dp[n]

    print(f'#{tc} {answer}')

