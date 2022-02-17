import sys

sys.stdin = open('input.txt')

def numbers_sort(args):
    n = len(args)
    for i in range(n):
        for j in range(n-1):
            if args[j] < args[j+1]:
                args[j], args[j+1] = args[j+1], args[j]
    return args

def danjo_test(num):
    while num//10 == 0:
        danjo_j = num%10



        num = num//10

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers_sort(numbers)

    rlt = 0
    i = 0

    for j in range(n):
        numbers[i]*



    print(f'#{tc} {rlt}')

