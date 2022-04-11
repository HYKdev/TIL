# 치킨 배달

from itertools import combinations

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = 0

chicken_lst = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            chicken_lst.append([i, j])
            matrix[i][j] = 0
for k in range(1, m+1):
    for chicken_place in combinations(chicken_lst, k):
        for i, j in chicken_place:
            matrix[i][j] = 2
        