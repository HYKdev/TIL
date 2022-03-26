import sys
sys.stdin = open('input.txt')

from collections import deque

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def BFS():
    q = deque()
    q.append()


# 입력
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]


    print(f'#{tc} ')