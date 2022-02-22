import sys

sys.stdin = open('input.txt')


T = int(input())

di = [0, 1, -1]
dj = [0, 1, -1]
for tc in range(1, T + 1):
    w, h = map(int, input().split())
    j, i = map(int, input().split())
    t = int(input())
    p = [i, j]
    d1 = 1
    d2 = 1
    while t > 0:
        power_j = w-j
        power_i = h-i
        ni = p[0] + di[d1]
        nj = p[1] + dj[d2]
        if nj == w or nj == 0:
            d2 = -d2
        if ni == h or ni == 0:
            d1 = -d1
        p = [ni, nj]
        t -= 1


    print(f'#{tc} {p[1]} {p[0]}')

