# 안테나


T = int(input())

antena_list = list(map(int, input().split()))

antena_list.sort()

print(antena_list[(T-1)//2])
