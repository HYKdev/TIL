# n 과 m (3)

from itertools import product

n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

for list in product(arr, repeat = m):
    print(*list)