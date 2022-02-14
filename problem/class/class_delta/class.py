import sys

sys.stdin = open('input.txt')

# 절대값 함수 선언
def num_abs(args):
    if args >= 0:
        return args
    else:
        return -args

# 좌우상하 방향 delta로 선언
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

# 테스트 케이스
T = int(input())

for tc in range(T):
    matrix = []
# 입력 값 데이터 정리
    n = int(input())
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

# 결과 초기화
    rlt = 0
# for 문을 통해 i,j 해서 행렬 탐색
# for 문 k를 통해서 방향 탐색
    for i in range(5):
        for j in range(5):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
# 인덱스 에러가 나는 범위를 설정하여 pass시킴
                if ni < 0 or ni > 4 or nj < 0 or nj > 4:
                    pass
# 인덱스 에러가 나지 않는 범위는 차이의 절대값을 결과값에 추가
                else:
                    sub = matrix[i][j] - matrix[ni][nj]
                    sub = num_abs(sub)

                    rlt += sub
# 결과 출력
    print(f'#{tc} {rlt}')
