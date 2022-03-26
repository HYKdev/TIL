# 이분 그래프

from collections import deque
import sys

# readline으로 인풋 안받으면 시간초과남
input = sys.stdin.readline

# BFS
def BFS(start):
    # q에 넣고 방문처리 후 while문 시작
    q = deque([start])
    visited[start] = 1

    # graph로 연결된 간선들 탐색해서
    # 방문 안했으면 -1 곱한 값으로 이분 그래프 확인
    # 간선으로 이어진 값이 서로 같다면 종료 ex) 1 <-> 1 / -1 <-> -1
    while q:
        point = q.popleft()
        for grap in graph[point]:
            if not visited[grap]:
                visited[grap] = -1 * visited[point]
                q.append(grap)
            elif visited[point] == visited[grap]:
                return False
    return True

# 입력
tc = int(input())
for _ in range(tc):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]        # graph 설정
    visited = [0 for _ in range(V+1)]       # 방문 설정
    for _ in range(E):                      # 간선 정보 입력
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V+1):                 # 방문 안했으면 BFS시작
        if not visited[i]:
            result = BFS(i)
            if not result:                  # BFS결과가 False이면 종료
                break
    
    print('YES' if result else 'NO')
    