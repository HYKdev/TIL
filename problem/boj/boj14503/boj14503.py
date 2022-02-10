import sys

sys.stdin = open('input.txt')

# 로봇 청소기
# N X M 행렬
# d 는 방향 0 북 1 동 2남 3서
# 청소한 구역은 2
# 

# args = 좌표, 방향
# r = row
# c = column
# d = 방향 0(-1, 0) / 1(0, 1) / 2(1, 0) / 3(0, -1)
def robot_clean(r, c, d):
    d1 = [-1, 0, 1, 0]
    d2 = [0, 1, 0, -1]
    while True:
        if data[r][c] == 0:
            data[r][c] = 2
        


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    
    robot_clean(r, c, d)

    print(f'#{tc} ')

