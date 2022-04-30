# 촌수 계산

# deque선언
from collections import deque

# BFS 함수
# q에 담고 방문처리후 q에 담겨있는게 없을 때까지 bfs반복
# q에서 꺼낸 후 촌수 끝인지 확인하고 아니면 BFS과정 반복
def BFS(start, end):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        i = q.popleft()
        if i == end:
            return visited[i]-1
        for j in graph[i]:
            if not visited[j]:
                visited[j] = visited[i] + 1
                q.append(j)
    return -1

# n명의 촌수 관계
# n명의 graph관계, n의 촌수 단계를 나타낼 visited
# a, b 입력을 통해 촌수 시작과 촌수 끝
# m개의 촌수 관계 및 m개의 그래프 관계
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
a, b = map(int, input().split())
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 결과 출력
result = BFS(a, b)
print(result)