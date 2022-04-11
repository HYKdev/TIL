# 회의실 배정

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()
arr = sorted(arr, key = lambda x : x[1])

time_i = 0
time_j = 0
cnt = 0
for i, j in arr:
    if time_j <= j and time_j <= i:
        time_j = j
        time_i = i
        cnt += 1

print(cnt)