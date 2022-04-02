import sys
sys.stdin = open('input.txt')

from itertools import permutations

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ans = 10000000
    arr = [i for i in range(1, n)]
    cart_list = []
    for lst in permutations(arr, n-1):
        cart_list.append([0] + list(lst) + [0])

    for i in range(len(cart_list)):
        total = 0
        for j in range(n):
            total += matrix[cart_list[i][j]][cart_list[i][j+1]]
        if ans > total:
            ans = total

    print(f'#{tc} {ans}')

