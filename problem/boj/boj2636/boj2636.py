# 치즈
# BFS로 문제를 해결하였고 cnt라는 변수를 둬서 bfs한번 돌 때 마다 치즈 녹는 개수를 체크하였습니다.
# q에 append해야 될 값과 matrix를 바꿔야 하는 값을 나눠서 잘 생각하면 어렵지 않은 문제라 생각합니다.
import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 방향 설정
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
cheese_list = []

# BFS 선언
def BFS():
# 초기 설정
    q = deque()
    q.append([0, 0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    cnt = 0

    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 범위 내 방문 하지 않았으면 방문한걸로 바꾸고
            # 치즈가 없으면 큐에 추가해서 탐색 계속하고
            # 치즈가 있으면 치즈 뺴고 cnt 추가
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                if matrix[ni][nj] == 0:
                    q.append([ni,nj])
                    
                elif matrix[ni][nj] == 1:
                    cnt += 1
                    matrix[ni][nj] = 0
                    
    cheese_list.append(cnt)
    return cnt

# 시간 체크
time = -1
while True:
    cnt = BFS()
    time += 1
# 반복문 종료 조건
    if cnt == 0:
        break

print(time)
print(cheese_list[-2])