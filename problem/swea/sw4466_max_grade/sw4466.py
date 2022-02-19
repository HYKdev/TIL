import sys

sys.stdin = open('input.txt')

def arr_sort(lst):
    m = len(lst)
    for i in range(m):
        for j in range(m-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    rlt = 0
    arr_sort(arr)

    for i in range(k):
        rlt += arr[i]

    print(f'#{tc} {rlt}')

