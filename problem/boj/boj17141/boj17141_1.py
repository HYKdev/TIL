# 선언
import sys
input = sys.stdin.readline

from collections import deque
from itertools import combinations

# 방향 벡터 선언
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

# BFS 함수
# 바이러스 시작점을 arr로 받아와서 q에 넣고
# bfs 돌려서 visited에 기록
def BFS(arr):
    q = deque()
    for pos in arr:
        q.append(pos)
        visited[pos[0]][pos[1]] = 1
    while q:
        [i, j] = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if matrix[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])

# 바이러스 체크 함수
# 바이러스가 도달하지 못한 곳을 체크하고 -1 추가
# 도달하지 못한 곳이 없다면
# 방문한 값중 가장 큰값을 리스트에 추가
def virus_check():
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and not matrix[i][j]:
                ans_list.append(-1)
                return
    time = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0 and time < visited[i][j]:
                time = visited[i][j]
    ans_list.append(time)
    return

# 입력
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 바이러스 가능한 포지션을 리스트화
# 그 다음 쉽게 계산하기 위해서 matrix에는 0으로 변환
virus_positive_position = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            virus_positive_position.append([i, j])
            matrix[i][j] = 0

# 바이러스 가능한 포지션 리스트를 m개 뽑은 리스트 lst [[],[],[]]
# nCr을 활용하여 가능한 경우의 수를 다 체크해서 ans_list에 결과를 담음
# 방문은 바이러스 위치가 바뀔 때 마다 새롭게 bfs돌려야 해서 초기화 함
ans_list = []
for lst in combinations(virus_positive_position, m):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    BFS(lst)
    virus_check()

# virus_check에 의해서 -1만 반환하면 -1을 출력하고
# 그게 아니라면 -1을 제외 하고 그중 가장 작은 값을 찾아 출력
# 시작점을 1로 잡아서 -1을 한 후 출력해야 정확한 값이 나옴 
if sum(ans_list) == -len(ans_list):
    print(-1)
else:
    ans = n * n
    for item in ans_list:
        if item > -1 and ans > item:
            ans = item
    print(ans-1)