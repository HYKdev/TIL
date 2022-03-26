# 적록색약

from collections import deque

# 4방향 선언
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

# BFS 선언
def BFS(x, y):

# 입력 값 받아서 입력 값과 같은 색깔 상하좌우 탐색해서 다 방문 처리
    visited[x][y] = 1
    q.append([x, y])
    while q:
        i, j = q.pop()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if matrix[ni][nj] == matrix[i][j]:
                    visited[ni][nj] = 1
                    q.append([ni,nj])


# BFS한번 할 때 마다 cnt 증가 함수
def color_cnt():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                BFS(i, j)
                cnt += 1
    return cnt

# 입력
n = int(input())
matrix = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
# RGB일때와 RB일때 각각 초기화 선언
cnt_RGB = 0
cnt_RB = 0

# BFS쓸 deque 선언
q = deque()

# BFS 돌려서 RGB일 때 갯수 count
cnt_RGB = color_cnt()

# RB일 때도 체크해야 해서 G를 R로 바꾸고 방문 초기화
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'

visited = [[0 for _ in range(n)] for _ in range(n)]

# BFS 돌려서 RB일 때 갯수 count
cnt_RB = color_cnt()

# 결과
print(cnt_RGB, cnt_RB)