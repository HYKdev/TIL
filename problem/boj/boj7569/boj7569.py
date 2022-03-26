# 토마토

import sys
from collections import deque


def BFS():
    # 토마토 리스트에 담겨 있는 좌표들 q에 담아서 cnt 체크
    q= deque()
    for point in tomato:
        q.append(point)
    cnt = -1

    while q:
        h,n,m = q.popleft()
        # 6방향 탐색해서 토마토 숙성 진행
        for l in range(6):
            nm = m + dm[l]
            nn = n + dn[l]
            nh = h + dh[l]
            if 0 <= nn < N and 0 <= nm < M and 0 <= nh < H and matrix[nh][nn][nm]== 0:
                q.append([nh,nn,nm])
                matrix[nh][nn][nm] += matrix[h][n][m] + 1
        # 6방향 끝날 때 마다 cnt 체크
        cnt = matrix[h][n][m] - 1

    # BFS 끝나고도 0이 있다면 -1 반환
    for z in matrix:
        for x in z:
            if 0 in x:
                return -1
    return cnt

# 입력
M, N, H = map(int, input().split())
# 3차원 방향 벡터
dm = [0, 0, 1, -1, 0, 0]
dn = [1, -1, 0, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
# 토마토 좌표담을 리스트 선언
tomato = []

# 3차원 행렬 입력 받기 및 토마토 좌표 담을 리스트에 추가
matrix = [[] for _ in range(H)]
for k in range(H):
    for i in range(N):
        matrix[k].append(list(map(int, input().split())))
        for j in range(M):
            if matrix[k][i][j] == 1:
                tomato.append([k, i, j])

print(BFS())