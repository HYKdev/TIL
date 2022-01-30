# 소인수분해
N = int(input())

i = 2
N_lists = []
while N>1:
    if N%i == 0:
        print(i)
        N = N//i
    else:
        i += 1

