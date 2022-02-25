import sys

sys.stdin = open('input.txt')

# 방향 탐색하기 위한 선언
T = int(input())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def miro_check(idx_i, idx_j):
# 결과 값을 마음대로 쓰기 위해 글로벌 변수 선언
# 가지치기가 가능한 위치를 저장하기 위해 스택 선언
    global result
    stack = [[idx_i, idx_j]]
    visit[idx_i][idx_j] = 1

# 스택에 저장된 위치가 없어질 때 까지 반복
    while stack:
        idx_i, idx_j = stack.pop()
# 방향 탐색해서 시작지점이 나오면 함수 종료
# 아니면 방문하지 않고 갈 수 있는 길이면 스택에 저장하고 방문한 곳 체크
        for k in range(4):
            ni = idx_i + di[k]
            nj = idx_j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] == 2:
                result = 1
                return
            if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] == 0 and not visit[ni][nj]:
                stack.append([ni, nj])
                visit[ni][nj] = 1
    result = 0
    return

# 테스트 케이스 입력
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
# 결과 값과 방문한 곳 선언
    result = 0
    visit = [[0 for _ in range(n)] for _ in range(n)]
# 도착지점 있으면 함수 실행 아니면 0 출력
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 3:
                miro_check(i, j)

    print(f'#{tc} {result}')

