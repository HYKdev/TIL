import sys

sys.stdin = open('input.txt')

def number_sort (args):
    for i in range(n):
        for j in range(n-1):
            if args[j] < args[j+1]:
                args[j], args[j+1] = args[j+1], args[j]
    return args

T = int(input())


for tc in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))

    number_sort(n_list)

    print(n_list[0]*n_list[-1])

