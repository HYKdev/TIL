import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1
    print(start, end= ' ')
    for V in graph[start]:
        if not visited[V]:
            DFS(V)

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(max(arr) + 1)]
    visited = [0 for _ in range(max(arr) + 1)]
    for i in range(0, len(arr), 2):
        graph[arr[i]].append(arr[i+1])
        graph[arr[i+1]].append(arr[i])

    print(f'#{tc}', end = ' ')
    DFS(1)