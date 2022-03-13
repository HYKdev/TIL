# 치즈
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
cheese_list = []

def BFS():
    q = deque()
    q.append([0,0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    cnt = 0

    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj]==0:
                visited[ni][nj] = 1
                if matrix[ni][nj] == 0:
                    q.append([ni,nj])
                    
                elif matrix[ni][nj] == 1:
                    cnt +=1
                    matrix[ni][nj] = 0
                    
    cheese_list.append(cnt)
    return cnt

time = -1
while True:
    
    cnt = BFS()
    time += 1
    if cnt == 0:
        break

print(time)
print(cheese_list[-2])