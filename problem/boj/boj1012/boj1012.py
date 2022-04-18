# 유기농 배추

from collections import deque
import sys

input = sys.stdin.readline

# 방향 벡터
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

# BFS함수
# 배추밭 위치를 q에 담았으니 BFS돌려서 1을 만날 때 마다 matrix값을 0으로 바꾸고
# q에 추가해서 상하좌우 연결되어 있는 모든 배추를 제거
def BFS():
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 1:
                matrix[ni][nj] = 0
                q.append([ni, nj])

# 입력
T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    # 유기농 배추 밭 행렬 선언
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    # BFS에 쓸 q 선언
    q = deque()
    # 유기농 배추 위치 입력 받아서 행렬에 할당
    for _ in range(k):
        c, r = map(int, input().split())
        matrix[r][c] = 1

    # 유기농 배추 밭 갯수 체크를 위해서 cnt초기화
    cnt = 0
    # 모든 행렬을 돌면서 BFS체크
    # 배추가 있으면 q에 넣고 BFS돈다음 밭 개수 1개 증가
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                q.append([i, j])
                BFS()
                cnt += 1

    print(cnt)
 