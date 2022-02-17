import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    data = []
    cnt = 0
    for _ in range(n):
        data.append(list(map(int, input().split())))

# 
    for i in range(n):
        len_cnt1 = 0
        for j in range(n):
            if data[i][j] == 0:
                if len_cnt1 == k:
                    cnt += 1
                len_cnt1 = 0
            else:
                len_cnt1 += 1
        if len_cnt1 == k:
            cnt += 1

    for i in range(n):
        len_cnt1 = 0
        for j in range(n):
            if data[j][i] == 0:
                if len_cnt1 == k:
                    cnt += 1
                len_cnt1 = 0
            else:
                len_cnt1 += 1
        if len_cnt1 == k:
            cnt += 1

    print(f'#{tc} {cnt}')

