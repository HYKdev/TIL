# 알파벳

import sys
input = sys.stdin.readline

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def DFS(i, j, cnt):
    global ans
    ans = max(ans, cnt)
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < r and 0 <= nj < c:
            if alpha[matrix[ni][nj]] == 0:
                alpha[matrix[ni][nj]] = 1
                DFS(ni, nj, cnt+1)
                alpha[matrix[ni][nj]] = 0

r, c = map(int, input().split())
matrix = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(r)]
alpha = [0] * 26

alpha[matrix[0][0]] = 1

ans = 1
DFS(0, 0, ans)
print(ans)