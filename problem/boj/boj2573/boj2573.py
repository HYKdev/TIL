import sys
from collections import deque

input = sys.stdin.readline

def BFS(lst):
    global ice_list, time
    q = deque()
    for ice in lst:
        q.append(ice)
    while q:
        visited = [[0 for _ in range(m)] for _ in range(n)]
        for _ in range(len(q)):
            i, j = q.popleft()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if not matrix[ni][nj] and not visited[ni][nj]:
                        if matrix[i][j] > 0:
                            matrix[i][j] -= 1
            visited[i][j] = 1
            if matrix[i][j] > 0:
                q.append([i, j])
        time += 1

        if not q:
            time = 0
            return
        
        result = BFS_test(q)
        if result:
            return
            
    time = 0
    return

def BFS_test(lst):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 1
    qq = deque()
    qq.append([lst[0][0], lst[0][1]])
    visited[lst[0][0]][lst[0][1]] = 1
    while qq:
        ii, jj = qq.popleft()
        for k in range(4):
            nii = ii + di[k]
            njj = jj + dj[k]
            if 0<= nii < n and 0 <= njj < m:
                if matrix[nii][njj] and not visited[nii][njj]:
                    cnt += 1
                    qq.append([nii, njj])
                    visited[nii][njj] = 1
    if len(lst) == cnt:
        return False
    else:
        return True

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
time = 0
ice_list = []
for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            ice_list.append([i, j])

BFS(ice_list)

print(time)