# 평균

n = int(input())
arr = list(map(int, input().split()))

max_value = max(arr)

total = 0

for item in arr:
    total += item/max_value*100

print(total/n)
