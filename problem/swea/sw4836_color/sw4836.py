import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

# 테스트 케이스 입력
for tc in range(1, T + 1):
    n = int(input())
# 좌표 범위가 9까지여서 10x10 0으로 된 행렬 선언
    data = [[0 for _ in range(10)] for _ in range(10)]

# 좌표 좌표 색깔 순서로 들어오기 때문에 각각의 값을 받아서 바로 활용
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

# 좌표 2개로 직사각형을 만드는 이중 for문을 구성하였고
# 행렬에 색깔에 맞는 color를 더하는 연산을 함
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                data[i][j] += color

# 보라색을 나타낼려면 두개의 색이 겹쳐 3이상인 것임으로
# for문을 돌려 3이상을 찾고 cnt로 추가
    cnt = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] >= 3:
                cnt += 1


    print(f'#{tc} {cnt}')

