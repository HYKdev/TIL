import sys

sys.stdin = open('input.txt')

def where_str(args):
    global k
    n = len(args)
    rlt = 0
    for arg in args:
        cnt = 0
        for i in range(n):
            if arg[i] == 1:
                cnt += 1
            else:
                if cnt == k:
                    rlt += 1
                cnt = 0
            if i == n-1 and cnt == k:
                rlt += 1
    return rlt
# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    data1 = []
    for _ in range(n):
        data1.append(list(map(int, input().split())))
    data2 = list(map(list, zip(*data1)))

    result = where_str(data1) + where_str(data2)

    print(f'#{tc} {result}')

