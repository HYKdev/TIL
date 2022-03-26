# 최소, 최대

n = int(input())

arr = list(map(int, input().split()))

max_num = arr[0]
min_num = arr[0]
for i in range(n):
    if arr[i] > max_num:
        max_num = arr[i]
    
    if arr[i] < min_num:
        min_num = arr[i]

print(min_num, max_num)