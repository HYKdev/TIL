# 나이트의 이동

from collections import deque

# 나이트가 갈 수 있는 방향 벡터 리스트
di = [-1, -2, -2, -1, 1, 2, 2, 1]
dj = [-2, -1, 1, 2, 2, 1, -1, -2]

# BFS시작
def BFS(start1, start2):
    # 덱으로 리스트 만들어 주고 스타트 지점 append, 방문처리
    q = deque()
    q.append([start1, start2])
    visited[start1][start2] = 1
    # q에 값이 있을 때 까지 반복문 진행
    while q:
        i, j = q.popleft()                                  # q의 가장 왼쪽 값 꺼내기
        for k in range(8):                                  # 나이트가 갈 수 있는 모든 방향 탐색
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:                 # 조건 : 갈 수 있는 범위내
                if not visited[ni][nj]:                     # 방문 안했으면 한단계 진행 후 방문 + 거리 체크
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])                      # q에 담아서 도착지점까지 알아낼 예정
                if ni == r2 and nj == c2:                   # 도착지점이면 위에서 체크한 거리 반환
                    return visited[ni][nj]

# 입력
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    visited = [[0 for _ in range(n)] for _ in range(n)]
    # 시작점과 도착점이 같으면 bfs연산 없이 처리하고
    # 아니면 bfs함수 돌려서 프린트
    # -1 하는 이유는 visited 시작점을 1로 시작해서 문제에 요구하는 것 보다 1이 더 높음
    if r1 == r2 and c1 == c2:
        print(0)
    else:
        print(BFS(r1, c1)-1)
