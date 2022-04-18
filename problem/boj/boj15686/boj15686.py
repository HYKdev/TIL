# 치킨 배달

from itertools import combinations

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')

chicken_lst = []
house_list = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            chicken_lst.append([i, j])

        elif matrix[i][j] == 1:
            house_list.append([i, j])


for k in range(1, m+1):
    for chicken_place in combinations(chicken_lst, k):
        total = 0
        for hi, hj in house_list:
            min_length = float('inf')
            for ci, cj in chicken_place:
                if abs(hi-ci) + abs(hj-cj) < min_length:
                    min_length = abs(hi-ci) + abs(hj-cj)
            total += min_length
            if answer < total:
                break
        if answer > total:
            answer = total
print(answer)
        