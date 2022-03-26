# 연결 요소의 개수

from collections import deque
import sys

input = sys.stdin.readline

def BFS(start):
    q.append(start)
    while q:
        point = q.popleft()
        for i in graph[point]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

q= deque()
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = 1
        BFS(i)
        cnt += 1

print(cnt)