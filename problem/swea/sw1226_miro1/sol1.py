import sys
sys.stdin = open('input.txt')

from collections import deque

# 4방향 탐색 벡터
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# BFS 선언
def BFS():
    # 스타트 지점 방문 처리후 q에 추가
    q = deque()
    q.append([1, 1])
    visited[1][1] = True

    # 방문하지 않았으면 방문처리하고 q에 추가하고
    # 반복문을 돌려 도착지점을 만나면 1반환 아니면 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 16 and 0 <= nj < 16 and not visited[ni][nj]:
                if matrix[ni][nj] == 0:
                    visited[ni][nj] = True
                    q.append([ni, nj])
                if matrix[ni][nj] == 3:
                    return 1
    return 0

# 테스트 케이스 입력
T = 10
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]
    visited = [[False for _ in range(16)] for _ in range(16)]

    print(f'#{tc} {BFS()}')

