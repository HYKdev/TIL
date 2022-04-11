# 연구소

from collections import deque
import sys
from itertools import combinations

input = sys.stdin.readline

# BFS 함수 virus좌표는 q
# copy한 matrix 활용
# 안전구역에서 바이러스가 늘어날수록 차감
def BFS(virus, deep_m, positive_area):
    q = deque()
    for i, j in virus:
        q.append([i, j])
        visited[i][j]= 1
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if not deep_m[nr][nc]:
                    positive_area -= 1
                    visited[nr][nc] = 1
                    q.append([nr, nc])
    return positive_area

# 방향 벡터
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
# 입력
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 바이러스 위치
# 벽을 둘 수 있는 위치
# 안전 구역 체크를 위한 빈공간 체크
virus_list = []
wall_pos = []
wall_number = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            virus_list.append([i, j])
        elif matrix[i][j] == 0:
            wall_pos.append([i, j])
            wall_number += 1

# 안전구역 결과 값 초기화
answer = 0

# 벽을 둘 수 있는 위치중에 3개를 뽑기
# 방문 초기화 deep_matrix로 copy하여 계속해서 matrix를 재활용 할 예정
# 3개 뽑은 벽을 deep_matrix에 적용 후 BFS 돌리기
# 나온 결과 값을 비교하여 최대값 갱신
for wall_three in combinations(wall_pos, 3):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    deep_matrix = [mat[:] for mat in matrix]
    for i, j in wall_three:
        deep_matrix[i][j] = 1
    cnt = BFS(virus_list, deep_matrix, wall_number)
    if answer < cnt:
        answer = cnt

# 벽 3개에 대한 값을 위에서 안 빼줬기에 결과에서 빼줌
print(answer-3)