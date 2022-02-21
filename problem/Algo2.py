import sys

sys.stdin = open('input_prob_2.txt')

# 사각형 더하기 델타 값
dx = [0, 0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 0, 0, -1, 1, 0, -1, 1]
# 3x3 배열 합 함수
def square_sum(lst):
    lst_sum = 0
    for i in range(1, n-1):
        for j in range(1, n-1):
            cnt = 0
            for k in range(9):
                cnt += lst[i+dx[k]][j+dy[k]]
            if lst_sum < cnt:
                lst_sum = cnt
    return lst_sum

# 테스트 케이스 입력
T = int(input())

# 4방향 탐색 델타
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for tc in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
# 최대값을 3x3의 합산으로 초기 설정 후 추후에 4방향 탐색과 비교할 예정
    max_sum = square_sum(arr)

# 인덱스 탐색
    for i in range(n):
        for j in range(n):
# 4방향 길이 설정 및 자신의 값을 cnt로 초기 설정
            d_range = arr[i][j] - 1
            arr_cnt = arr[i][j]
# 4방향 합산 반복문 가장 바깥쪽 위치부터 안쪽으로 더할 예정
# 인덱스 에러 나면 pass
            while d_range > 0:
                for k in range(4):
                    ni = i + di[k]*d_range
                    nj = j + dj[k]*d_range
                    if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                        pass
                    else:
                        arr_cnt += arr[ni][nj]
                d_range -= 1

# 최댓값 비교
            if max_sum < arr_cnt:
                max_sum = arr_cnt

    print(f'#{tc} {max_sum}')

