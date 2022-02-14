import sys

sys.stdin = open('input.txt')

T = 10

# 테스트 케이스 입력
for tc in range(1, T + 1):
    n = int(input())
    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))

# 조건에 맞는 합산 리스트 초기화
    matrix_sum = []
# 행1줄 or 열 1줄 합산을 리스트에 추가
# 행1줄 or 열 1줄 합산 추가 후 0으로 초기화 해야 연산이 안 겹침
    for i in range(100):
        sum1 = 0
        sum2 = 0
        for j in range(100):
            sum1 += matrix[j][i]
            sum2 += matrix[i][j]
        matrix_sum.append(sum1)
        matrix_sum.append(sum2)

# 대각선 합산 계산
    sum3 = 0
    sum4 = 0
    for i in range(100):
        for j in range(100):
# 왼쪽에서 오른쪽 대각선 조건
            if i == j:
                sum3 += matrix[i][j]
# 오른쪽에서 왼쪽 대각선 조건
            if i + j == 99:
                sum4 += matrix[i][j]
    matrix_sum.append(sum3)
    matrix_sum.append(sum4)

# max 찾기 기준은 리스트 첫번째 값
    max_sum = matrix_sum[0]

# 최댓값 찾기
    for i in range(len(matrix_sum)):
        if matrix_sum[i] >= max_sum:
            max_sum = matrix_sum[i]

# 출력
    print(f'#{tc} {max_sum}')

