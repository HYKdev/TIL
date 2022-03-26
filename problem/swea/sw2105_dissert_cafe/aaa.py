import sys
sys.stdin = open('input.txt')

directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
def dfs(i, j, direction_type, dessert_cnt):
    global ans
    if direction_type < 3:
        tmp = direction_type + 2
    else: tmp = direction_type + 1

    for k in range(direction_type, tmp):
        ni = i + directions[k][0]
        nj = j + directions[k][1]

        if start[0] == ni and start[1] == nj:
            ans = max(ans, dessert_cnt)
            return

        if 0 <= ni < N and 0 <= nj < N:
            if dessert_visited[arr[ni][nj]] == False:
                dessert_visited[arr[ni][nj]] = True

                dfs(ni, nj, k, dessert_cnt + 1)

                dessert_visited[arr[ni][nj]] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    dessert_visited = [False] * 101
    ans = -1
    for i in range(N):
        for j in range(N):
            start = (i, j)
            dessert_visited[arr[i][j]] = True

            dfs(i, j, 0, 1)

            dessert_visited[arr[i][j]] = False

    print(f'#{tc} {ans}')

