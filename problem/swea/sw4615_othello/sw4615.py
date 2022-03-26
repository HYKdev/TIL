import sys
import pprint
sys.stdin = open('input.txt')

# 오셀로 함수
def othello(p_i, p_j, p_color):
    # 흑돌이면 백돌 테스트
    # 백돌이면 흑돌 테스트
    if p_color == 1:
        test_color = 2
    else:
        test_color = 1

    # 8방향 탐색 및 스택 초기화
    for k in range(8):
        ni = p_i + di[k]
        nj = p_j + dj[k]
        stack = []
        # 한 방향으로 계속 진행하기 위해서 while True 이용
        while True:
            # 범위 밖으로 나가면 스택 초기화하고 반복문 종료
            if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                stack = []
                break
            # 탐색 중 돌이 없다면 스택 초기화하고 반복문 종료
            if matrix[ni][nj] == 0:
                stack = []
                break
            # 돌 놓은 색깔과 다른 색깔이면 스택에 담기
            if matrix[ni][nj] == test_color:
                stack.append([ni, nj])
            # 돌 놓은 색깔과 같은 색깔이면 반복문 종료
            elif matrix[ni][nj] == p_color:
                # 스택에 담긴걸 꺼내서 돌 체인지
                for p_ii, p_jj in stack:
                    matrix[p_ii][p_jj] = p_color
                break
            # 한방향으로 계속 진행하기 위해서 방향 벡터 계속 더하기
            ni += di[k]
            nj += dj[k]


T = int(input())
di = [0, 0, 1, 1, 1, -1, -1, -1]
dj = [1, -1, 0, 1, -1, 0, 1, -1]

# 테스트 케이스 입력
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    # 흑돌 백돌 시작점 세팅
    matrix[n//2-1][n//2-1], matrix[n//2][n//2] = 2, 2
    matrix[n//2-1][n//2], matrix[n//2][n//2-1] = 1, 1

    # 좌표 받은 후 그 자리에 돌이 없다면 오셀로 시작
    for _ in range(m):
        j, i, color = map(int, input().split())
        i -= 1
        j -= 1
        if not matrix[i][j]:
            matrix[i][j] = color
            othello(i, j, color)

    # 흑돌 백돌 카운트
    ans_black = 0
    ans_white = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                ans_black += 1
            elif matrix[i][j] == 2:
                ans_white += 1

    # 출력
    print(f'#{tc} {ans_black} {ans_white}')