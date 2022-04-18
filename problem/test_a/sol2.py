import sys
sys.stdin = open('input2.txt')


from collections import deque

def BFS(r, c, hard):
    global ans
    q = deque()
    q.append([r, c, hard])
    visited[r][c] = 1
    while q:
        i, j, h = q.popleft()
        if matrix[i][j] == 3:
            ans.append(h)

        for l in range(1, n):
            for k in range(2):
                ni = i + di[k] * l
                nj = j
                if 0 <= ni < n and 0 <= nj < m:
                    if matrix[ni][nj] and not visited[ni][nj]:
                        if l > h:
                            hard = l
                        else:
                            hard = h

                        visited[ni][nj] = hard
                        q.append([ni, nj, hard])

                    elif matrix[ni][nj] and visited[ni][nj]:
                        if visited[ni][nj] > h:
                            q.append([ni, nj, h])
                            visited[ni][nj] = h

            for k in range(2, 4):
                ni = i
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if matrix[ni][nj] and not visited[ni][nj]:
                        visited[ni][nj] = h
                        q.append([ni, nj, h])
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    ans = []

    BFS(4, 0, 1)
    print(ans)
    print(f'#{tc} {min(ans)}')

