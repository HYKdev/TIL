#외계인의 기타 연주

import sys

n, p = map(int, sys.stdin.readline().split())

lst = [[] for _ in range(n+1)]
cnt = 0
for _ in range(n):
    sound, fret = map(int, sys.stdin.readline().split())
    if len(lst[sound]) == 0 or lst[sound][-1] < fret:
        cnt += 1
        lst[sound].append(fret)
    elif lst[sound][-1] > fret:
        while True:
            if len(lst[sound]) == 0 or lst[sound][-1] < fret:
                cnt += 1
                lst[sound].append(fret)
                break
            if lst[sound][-1] == fret:
                break
            lst[sound].pop()
            cnt += 1
print(cnt)