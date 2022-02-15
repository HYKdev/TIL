# Ladder1
import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
for _ in range(10):
    n = int(input())
# 방향 위 좌 우
    di = [-1, 0, 0]
    dj = [0, -1, 1]
    d = 0
    data = []
    for _ in range(100):
        data.append(list(map(int, input().split())))

# 도착지점 기준으로 출발지점까지 가기 위해서 도착지점 선별
    i = 99
    for k in range(100):
        if data[99][k] == 2:
            j = k

    while True:
# 출발지점 도착시 종료
        if i == 0:
            break
# 위로 올라가다가 좌,우 사다리를 만나면 방향 값 변환
        if d == 0:
            if j >= 1 and data[i][j-1] == 1:
                d = 1
            elif j <= 98 and data[i][j+1] == 1:
                d = 2
# j방향으로 0을 만날 때 방향전환으로 할려면
# data 리스트 양쪽에 0을 추가해야함
# 좌로 가다가 위 방향에 1을 만나면 위로 전환
        elif d == 1:
            if data[i-1][j] == 1:
                d = 0
# 우로 가다가 위 방향에 1을 만나면 위로 전환
        else:
            if data[i-1][j] == 1:
                d = 0

# 방향 값에 따른 인덱스 변화
        i += di[d]
        j += dj[d]


    print(f'#{n} {j}')

