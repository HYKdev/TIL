# 스타트와 링크

from itertools import combinations


n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

arr = [i for i in range(n)]

for lst in combinations(arr,  n//2):
    print(lst)