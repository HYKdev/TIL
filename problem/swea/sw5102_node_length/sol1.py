import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

# BFS 선언
# 시작지점을 q에 넣고 BFS 반복하여
# 도착지점이면 함수를 종료하고
# 아니면 graph에 있는 노드 연결 정보를 활용하여
# q에추가하고 visited 값 변경
def BFS():
    q = deque()
    q.append(start)
    while q:
        point = q.popleft()
        if point == end:
            return visited[point]

        for i in graph[point]:
            if not visited[i]:
                print(visited)
                visited[i] = visited[point] + 1
                q.append(i)

    return 0

# 테스트 케이스 입력
# graph는 노드간의 연결리스트
# visited는 방문 확인 및 이동한 횟수 체크
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    start, end = map(int, input().split())

    print(f'#{tc} {BFS()}')

