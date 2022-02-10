import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

# 결과 값, 연속하는 값의 최대 값, 최소 값 초기화
# 연속하는 최소 값 기준 잡기
    ans = 0
    sum_max = 0
    sum_min = 0
    for j in range(M):
        sum_min += numbers[j]

# 이중 for문을 돌려서 기준되는 값보다 크면 max 작으면 min에 계속 저장
    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += numbers[i+j]
        if sum > sum_max:
            sum_max = sum
        if sum < sum_min:
            sum_min = sum

    ans = sum_max - sum_min
    print(f'#{tc} {ans}')

