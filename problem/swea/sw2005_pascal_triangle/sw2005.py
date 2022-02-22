import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n = int(input())

# 10x10 행렬 선언
    arr = [[1 for _ in range(10)] for _ in range(10)]

# 파스칼 삼각형에 따른 행렬의 값 변환
    for i in range(2, n):
        for j in range(1, i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

# 출력
    print(f'#{tc}')
    for i in range(n):
        print(*arr[i][0:i+1])



