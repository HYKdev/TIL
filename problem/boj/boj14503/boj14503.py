import sys

sys.stdin = open('input.txt')

# 로봇 청소기
# N X M 행렬
# 청소한 구역은 2

# r = row, c = column
# d = 방향 0북(-1, 0) / 1동(0, 1) / 2남(1, 0) / 3서(0, -1)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def robot_clean(r, c, d):

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    
    # print(f'#{tc} ')

