#Farm


a, b, n, w = map(int, input().split())

arr = []
for i in range(1, n):
    if (a*i + b*(n-i) == w): arr.append([i,n-i])
if len(arr) == 1:
    print(arr[0][0],arr[0][1])
else:
    print(-1)

