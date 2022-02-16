import sys

sys.stdin = open('input.txt')

T = int(input())

def max_num_sum(args):
    max_number = args[0]
    max_sum = 0
    for i in range(1, n):
        if max_number > args[i]:
            max_sum += max_number - args[i]
        else:
            max_number = args[i]
    return max_sum

for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))[::-1]

    rlt = max_num_sum(numbers)

    print(f'#{tc} {rlt}')

