import sys

sys.stdin = open('input_prob_1.txt')

# 행 인덱스 <= 열의 인덱스 <= R+k-1

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

#결과 값 초기화
    max_sum = 0

# 각 행 별로 합산 찾아서 비교 후 최댓값 정하기
    for i in range(n):
        cnt = 0
        for j in range(i, i+k):
            if j < n:
                cnt += arr[i][j]
        if max_sum < cnt:
            max_sum = cnt

    print(f'#{tc} {max_sum}')

