import sys
sys.stdin = open('input.txt')

from collections import deque
def BFS(start):

    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        visited[v] = 1
        for item in graph[v]:
            if not visited[item]:
                q.append(item)

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0 for _ in range(n + 1)]
    graph = [[] for _ in range(n+1)]
    cnt = 0
    for i in range(0, len(arr), 2):
        graph[arr[i]].append(arr[i+1])
        graph[arr[i+1]].append(arr[i])

    for i in range(1, n+1):
        if not visited[i]:
            BFS(i)
            cnt += 1
    print(f'#{tc} {cnt}')

