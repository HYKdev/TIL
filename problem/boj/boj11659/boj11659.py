# 구간 합 구하기 4

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = [0 for _ in range(n+1)]
total = 0
for i in range(1, n+1):
    total += arr[i-1]
    arr_sum[i] = total

for _ in range(m):
    start, end = map(int, input().split())
    print(arr_sum[end] - arr_sum[start-1])