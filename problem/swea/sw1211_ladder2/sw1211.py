import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    n = int(input())
    data = []
    for _ in range(100):
        data.append([0] + list(map(int, input().split())) + [0])

    min_move = 9999999
    min_start = 0

# start, end point 선언
    for k in range(100):
        i = 99
        j = k
        cnt = 0

# 출발점이 0인 부분은 while문 실행 x
        if data[i][j] == 0:
            continue

# 출발지점 도착하면 break
        while True:
            if i == 0:
                break

# 좌 조건 및 위 조건 나올때 까지 진행
            if data[i][j - 1] == 1:
                while True:
                    j -= 1
                    cnt += 1
                    if data[i][j - 1] == 0:
                        break

# 우 조건 및 위 조건 나올때 까지 진행
            elif data[i][j + 1] == 1:
                while True:
                    j += 1
                    cnt += 1
                    if data[i][j + 1] == 0:
                        break

# 위 조건 및 좌우 조건이 아니면 위로 진행
            i -= 1
            cnt += 1

# 최솟값은 idx값과 최솟값 저장
        if cnt < min_move:
            min_move = cnt
            min_start = j

# 처음에 0을 넣어줘서 idx값 1 빼야함
    print(f'#{tc} {min_start-1}')