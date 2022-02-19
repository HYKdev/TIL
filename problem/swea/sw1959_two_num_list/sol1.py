import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    rlt = 0

    if n > m:
        n, m = m, n
        n_list, m_list = m_list, n_list
    max_sum = 0
    j = 0

    while j < m-n+1:
        sum_list = 0

        for i in range(n):
            sum_list += n_list[i]*m_list[i+j]

        if max_sum < sum_list:
            max_sum = sum_list

        j += 1

    print(f'#{tc} {max_sum}')

