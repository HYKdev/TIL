# 이항 계수 1

n, k = map(int, input().split())

ans = 1
for i in range(n,1,-1):
    ans *= i

for j in range(1, k+1):
    ans /= j

for k in range(1, n-k+1):
    ans /= k
print(int(ans))