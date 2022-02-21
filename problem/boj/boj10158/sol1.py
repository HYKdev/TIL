import sys

sys.stdin = open('input.txt')


T = int(input())

di = [1, -1, 1, -1]
dj = [1, 1, -1, -1]
for tc in range(1, T + 1):
    w, h = map(int, input().split())
    j, i = map(int, input().split())
    t = int(input())

    while t > 0:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 < ni < h and 0 < nj < w:
                

    print(f'#{tc} ')

