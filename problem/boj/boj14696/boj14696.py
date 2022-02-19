# import sys

# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    A_count = [0 for _ in range(5)]
    B_count = [0 for _ in range(5)]

    for i in range(1, len(A_list)):
        A_count[A_list[i]] += 1
    for i in range(1, len(B_list)):
        B_count[B_list[i]] += 1

    result = 'D'
    for i in range(4,0,-1):
        if A_count[i] > B_count[i]:
            result = 'A'
            break
        elif A_count[i] < B_count[i]:
            result = 'B'
            break
    print(f'{result}')

