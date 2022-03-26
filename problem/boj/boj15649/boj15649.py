# n과 m (1)

from itertools import combinations, permutations

n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

for i in permutations(arr, m):
    print(*i)
