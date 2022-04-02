import sys
sys.stdin = open('input.txt')

# 오른쪽, 아래 방향 벡터
di = [0, 1]
dj = [1, 0]

# DFS + 백트래킹
def DFS(i, j):
    # ans와 total을 글로벌 선언하여 종료 조건에 사용할 예정
    global ans, total
    if ans < total:                         # 저장된 ans보다 total이 크면 더하는 의미가
        return                              # 없어서 종료

    if i == n-1 and j == n-1:               # 도착하면 ans에 total값 저장하고 종료
        ans = total
        return

    for k in range(2):                      # 2방향 탐색 하여 방문 하지 않았으면
        ni = i + di[k]                      # 방문처리하고 합산 후 DFS()호출
        nj = j + dj[k]                      # 백트래킹을 위해서 방문제거 + total 이전 값 제거
        if 0 <= ni < n and 0 <= nj < n:
            if not visited[ni][nj]:
                visited[ni][nj] = 1
                total += matrix[ni][nj]
                DFS(ni, nj)
                visited[ni][nj] = 0
                total -= matrix[ni][nj]

# 입력
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    # 합산의 시작은 0,0에서 시작하기 때문에 초기 값을 matrix[0][0]으로 시작함
    total = matrix[0][0]

    # 초기 ans를 matrix의 총 합으로 둬서 최소 값을 찾아 나갈 예정
    # 결과는 matrix의 총합보다는 작기 때문에 최소 값 찾기 기준으로 잡았음.
    ans = 0
    for mat in matrix:
        ans += sum(mat)

    # DFS 시작
    DFS(0, 0)
    print(f'#{tc} {ans}')
