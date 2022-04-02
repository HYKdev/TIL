# 블랙잭

from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for lst in combinations(arr, 3):
    if sum(lst) <= m:
        ans = max(ans, sum(lst))

print(ans)