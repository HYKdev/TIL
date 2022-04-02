# 물통

from collections import deque
import sys
input = sys.stdin.readline

def BFS(start):
    q = deque()
    q.append(start)
    while q:
        k = q.popleft()
        if not k in result:
            result.append(k)
            q.append()

a, b, c = map(int, input().split())

water_list = [0, 0, c]
result = []

BFS(c)