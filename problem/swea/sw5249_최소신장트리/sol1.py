import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        matrix[n1][n2] = w
        matrix[n2][n1] = w

    INF = float('inf')
    key = [INF] * (V+1)
    p = [-1] * (V+1)
    visited = [False] * (V+1)

    key[0] = 0
    cnt = 0
    result = 0

    while cnt < V+1:
        min = INF
        u = -1
        for i in range(V+1):
            if not visited[i] and key[i] < min:
                min = key[i]
                u = i
        visited[u] = True
        result += min
        cnt += 1

        for j in range(V+1):
            if matrix[u][j] > 0 and not visited[j] and key[j] > matrix[u][j]:
                key[j] = matrix[u][j]
                p[j] = u

    print(f'#{tc} {result}')

