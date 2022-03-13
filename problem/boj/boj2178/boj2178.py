# 미로 탐색


from collections import deque


N, M = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(N)]
count = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
queue = deque([[0, 0]])
visited[0][0] = True
count[0][0] = 1
while queue:
    [i, j] = queue.popleft()
    if i == N-1 and j == M-1:
        break
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and matrix[ni][nj] == 1:
            queue.append([ni, nj])
            visited[ni][nj] = True
            count[ni][nj] += count[i][j] + 1
print(count[N-1][M-1])
