# 바이러스

from collections import deque


def dfs(n):
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

def BFS(n):
    q = deque()
    visited[n] = True
    q.append(n)
    while q:
        V = q.pop()
        for i in graph[V]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


computer = int(input())
number = int(input())

graph = [[] for _ in range(computer+1)]
visited = [False for _ in range(computer+1)]

for _ in range(number):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(1)
print(visited.count(True)-1)
visited = [False for _ in range(computer+1)]

print(BFS(1))

print(visited.count(True)-1)
