import sys

sys.stdin = open('input.txt')

def dfs():
    global result

    return result
# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    check_list = [False for _ in range(n)]
    result = 0

    print(f'#{tc} {result}')

