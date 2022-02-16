import sys

sys.stdin = open('input.txt')

def max_circular_even(lst):
    max_len = 0
    for i in range(len(lst) - 1):
        cnt = 0
        if lst[i] == lst[i + 1]:
            cnt += 2
            j = 1
            while i + j + 1 < len(lst):
                if i-j >= 0 and lst[i - j] == lst[i + j + 1]:
                    cnt += 2
                    j += 1
                else:
                    break
        if max_len < cnt:
            max_len = cnt
    return max_len


def max_circulat_odd(lst):
    max_len = 0
    for i in range(len(lst)):
        cnt = 1
        j = 1
        while i + j < len(lst):
            if i-j >= 0 and lst[i - j] == lst[i + j]:
                cnt += 2
                j += 1
            else:
                break
        if max_len < cnt:
            max_len = cnt
    return max_len

# 테스트 케이스 입력
for tc in range(1, 11):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(100)]
    ans = 0

# 최대 값 비교
    for i in range(100):  # 행 회문 판별
        max_even = max_circular_even(arr[i])
        if max_even > ans:
            ans = max_even
        max_odd = max_circulat_odd(arr[i])
        if max_odd > ans:
            ans = max_odd

# 최대 값 비교
    for j in range(100):  # 열 회문 판별
        col_lst = []
        for i in range(100):
            col_lst.append(arr[i][j])
        max_even = max_circular_even(col_lst)
        if max_even > ans:
            ans = max_even
        max_odd = max_circulat_odd(col_lst)
        if max_odd > ans:
            ans = max_odd

    print(f'#{tc} {ans}')