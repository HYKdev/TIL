# 검증수

arr = list(map(int, input().split()))

total = 0

for item in arr:
    total += item**2

print(total%10)