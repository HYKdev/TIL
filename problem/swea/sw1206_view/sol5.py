import sys

sys.stdin = open('input5.txt')

# 테스트 케이스 개수
T = 10

# 입력
# 데이터를 리스트로 변환하여 입력
# 결과 값 초기화
for tc in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    result = 0

# 기준점에서 첫 번째 왼쪽(오른쪽), 두 번째 왼쪽(오른쪽) 차이 값이 0보다 커야 조망권이 있다.
# 그 차이 값 중에서 작은 값이 조망권이 있는 층수로 계산
    for i in range(2, n-2):
        left_view = 0
        right_view = 0
        a = n_list[i] - n_list[i-1]
        b = n_list[i] - n_list[i-2]
        c = n_list[i] - n_list[i+1]
        d = n_list[i] - n_list[i+2]
        if a > 0 and b > 0:
            if a > b:
                left_view = b
            else:
                left_view = a

        if c > 0 and d > 0:
            if c > d:
                right_view = d
            else:
                right_view = c

# 층수가 0이하이면 조망권이 없고
# 층수가 왼,오 둘다 1이상이면 작은 기준으로 조망권을 가지고 합산하여 출력
        if left_view <= 0 or right_view <= 0:
            result += 0
        elif left_view > right_view:
            result += right_view
        elif left_view <= right_view:
            result += left_view

    print(f'#{tc} {result}')

