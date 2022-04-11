# 동전 0

def coin_cnt():
    global n, k, arr, cnt_lst
    for i in range(n-1, -1, -1):
        if arr[i] <= k:
           while arr[i] <= k:
               k -= arr[i]
               cnt_lst[i] += 1
        if k == 0:
            return

n, k = map(int, input().split())
arr= []
cnt_lst = [0 for _ in range(n)]
for _ in range(n):
    arr.append(int(input()))

coin_cnt()

print(sum(cnt_lst))