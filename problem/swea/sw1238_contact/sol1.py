import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS():
    # 시작점 넣고 이동 거리 초기 값 1로 잡고 bfs시작
    q = deque()
    q.extend(graph[start])
    cnt = 1
    while q:
        cnt += 1
        for _ in range(len(q)):                 # q에 넣은 만큼만 돌리고 다시 넣기를 반복해야
            contact_point = q.popleft()         # 이동 거리 체크가 가능함
            if not visited[contact_point]:      # 방문 안했으면 q에 넣고 이동거리 체크
                q.extend(graph[contact_point])
                visited[contact_point] += cnt
    return

# 입력
T = 10
for tc in range(1, T + 1):
    number, start = map(int, input().split())
    arr = list(map(int, input().split()))
    # 연결 리스트 선언
    # 방문 체크 및 이동한 거리
    # 시작점을 방문 1로 잡고 거리 체크
    graph = [[] for _ in range(number+1)]
    visited = [0 for _ in range(number+1)]
    visited[start] = 1
    # arr로 받은 리스트를 graph 연결리스트 넣기
    for i in range(0, len(arr), 2):
        graph[arr[i]].append(arr[i+1])

    BFS()
    # 인덱스 큰 값부터 탐색해서 거리가 가장 높은 것을 ans에 담기
    ans = 0
    for i in range(len(visited)-1, 0, -1):
        if visited[i] == max(visited):
            ans = i
            break

    print(f'#{tc} {ans}')

