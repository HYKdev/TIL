# 약수들의 합

while True:
    n = int(input())

    if n == -1:
        break

    n_list = []
    for i in range(1,n):
        if n%i == 0:
            n_list.append(i)

    if sum(n_list) == n:
        print(n,'=', end=' ')
        for j in range(len(n_list)-1):
            print(n_list[j], '+', end=' ')
        print(n_list[-1])
    else:
        print(f'{n} is NOT perfect.')

    
