# 소수 구하기

m ,n = map(int, input().split())
n += 1
count_list = [True]*n

for i in range(2, int(n**0.5)+1):
    if count_list[i]:
        for j in range(2*i, n, i):
            count_list[j] = False

for i in range(m, n):
    if i > 1 and count_list[i] == True:
        print(i)

