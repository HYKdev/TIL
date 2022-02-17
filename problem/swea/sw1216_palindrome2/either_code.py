import sys

sys.stdin = open('input.txt')

# 최대 길이가 짝수인 회문 탐색
def max_circular_even(lst):
    max_len = 0
    for i in range(len(lst) - 1):
        cnt = 0
        if lst[i] == lst[i + 1]:
            cnt += 2
            j = 1
            while i + j + 1 < len(lst):
                if i-j >= 0 and lst[i - j] == lst[i + 1 + j]:
                    cnt += 2
                    j += 1
                else:
                    break
        if max_len < cnt:
            max_len = cnt
    return max_len

# 최대 길이가 홀수인 회문 탐색
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

# 최댓값 비교 함수
def max_test(lst):
# 글로벌 변수를 선언하여 마음대로 사용
    global ans
    for i in range(100):
        max_even = max_circular_even(lst[i])
        if max_even > ans:
            ans = max_even
        max_odd = max_circulat_odd(lst[i])
        if max_odd > ans:
            ans = max_odd

    return ans

# 테스트 케이스 입력
for tc in range(1, 11):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(100)]
    ans = 0
# transpose
    col_lst = list(map(list, zip(*arr)))

# 최대 값 함수 호출
    max_test(arr)
    max_test(col_lst)

    print(f'#{tc} {ans}')