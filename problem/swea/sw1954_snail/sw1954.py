import sys
import pprint
sys.stdin = open('input.txt')

T = int(input())
# 테스트 케이스 입력
for tc in range(1, T + 1):
    n = int(input())
# 우 하 좌 상 순으로 진행
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
# 빈 매트릭스 선언
    matrix = [[0 for _ in range(n)] for _ in range(n)]
# row, col, 방향, 매트릭스에 넣을 숫자 선언
    r = 0
    c = 0
    d = 0
    cnt = 1

    while True:
# 매트릭스 다 채우면 종료
        if cnt == n*n+1:
            break
        matrix[r][c] = cnt
        cnt += 1

# 방향 탐색
        for i in range(2):
            d = (d+i) % 4
            nr = r + dr[d]
            nc = c + dc[d]
# 밖으로 넘어가지 않고 다음 방향에 값이 0이여야 진행
            if 0 <= nc < n and 0 <= nr < n and matrix[nr][nc] == 0:
                r, c = nr, nc
                break

# 원하는 출력을 얻기 위해서 이중 for문 과 end 및 띄어쓰기 추가
    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = " ")
        print()

