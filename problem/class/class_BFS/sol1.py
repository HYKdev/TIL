import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        V = q.popleft()
        print(V, end = ' ')
        for item in graph[V]:
            if not visited[item]:
                q.append(item)
                visited[item] = 1

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(max(arr) + 1)]
    visited = [0 for _ in range(max(arr) + 1)]
    for i in range(0, len(arr), 2):
        graph[arr[i]].append(arr[i+1])
        graph[arr[i+1]].append(arr[i])


    print(f'#{tc} ', end= '')
    BFS(1)
