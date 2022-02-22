import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    m_list = list(map(int, input().split()))


    print(f'#{tc} ')

