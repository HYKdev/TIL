
import sys

n, p = map(int, sys.stdin.readline().split())

lst = [[0] for _ in range(7)]
cnt = 0
for _ in range(n):
    sound, fret = map(int, sys.stdin.readline().split())
    while lst[sound][-1] > fret:
        lst[sound].pop()
        cnt += 1
    if lst[sound][-1] != fret:
        lst[sound].append(fret)
        cnt += 1
print(cnt)
