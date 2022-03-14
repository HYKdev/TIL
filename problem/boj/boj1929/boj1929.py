# 소수 구하기

m ,n = map(int, input().split())

count_list = [True for _ in range(n+1)]

n_sqrt = int(n**0.5)
for i in range(2,n_sqrt+1):
    if count_list[i] == True:
        for j in range(i+i, n, i):
            count_list[j] = False

for i in range(m, n):
    if count_list[i] == True:
        print(i)

