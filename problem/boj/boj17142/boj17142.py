# 82%에서 터짐 (첫번째 반례)
# 92%에서 터짐 (두번째 반례)
"""
5 1
0 2 2 2 0
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
# 2

4 4
1 1 1 1
1 2 2 1
1 2 2 1
1 1 1 1
# 0
"""

# 모듈 및 클래스 선언
import sys
input = sys.stdin.readline

from collections import deque
from itertools import combinations

# 방향 벡터
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

# BFS 함수
# 바이러스 출발지점을 arr로 받아서 q에 넣고
# bfs 돌리기
# 연구소2랑 다르게 바이러스 자리를 그대로 살려둬서 벽이 아니면 방문 처리
def BFS(arr):
    q = deque()
    for ar in arr:
        q.append(ar)
        visited[ar[0]][ar[1]] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if not visited[ni][nj] and matrix[ni][nj] != 1:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])

# 바이러스 체크 함수
# 바이러스 스타트 지점과 벽이 아니고 방문한 적이 없다면 -1
# time = 1로 잡은 이유는 matrix로 주는 값에 0이 하나도 없는 경우
# 다 방문처리가 1인데 내 코드에서 time 갱신을 못해서 오류가 난다.
def virus_check():
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and matrix[i][j] == 0:
                ans_list.append(-1)
                return

    time = 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] and matrix[i][j] == 0 and time < visited[i][j]:
                time = visited[i][j]
    ans_list.append(time)

# 입력
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 바이러스 가능한 포지션들 좌표 받기
virus_positive_position = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            virus_positive_position.append([i, j])

# 가능한 시간 리스트 받기
# nCr로 가능한 포지션을 잡고 BFS와 virus_check를 해서 ans_list 담기
ans_list = []
for lst in combinations(virus_positive_position, m):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    BFS(lst)
    virus_check()

# 가능한 경우가 없다면 -1
# 가능한 경우가 있다면 -1 제외한 가장 작은 값을 할당해서 프린트
if sum(ans_list) == -len(ans_list):
    print(-1)
else:
    min_time = n * n
    for item in ans_list:
        if item > -1 and min_time > item:
            min_time = item

    print(min_time-1)