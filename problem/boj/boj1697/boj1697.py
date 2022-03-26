# 숨바꼭질

from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
distance = [0 for _ in range(10**5+1)]

def BFS(start):
    q = deque()
    q.append(start)
    while q:
        i = q.popleft()
        if i == k:
            return distance[i]

        for ni in [i-1, i+1, 2* i]:
            if 0<= ni <= 10**5 and not distance[ni]:
                distance[ni] = distance[i] + 1
                q.append(ni)

print(BFS(n))