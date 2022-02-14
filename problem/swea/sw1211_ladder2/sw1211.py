import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    n = int(input())
    data = []
    for _ in range(100):
        data.append(map(int, input().split()))
    result = 0
    start = 0
# start 지점 찾기
    for j in range(100):
        if data[0][j] == 1:
            start = j
            cnt = 0
            i = 0
        while True:
            if i == 99:
                break
            if 0 < j < 97 and data[i][j+1] == 1:
                





    print(f'#{tc} {result}')

