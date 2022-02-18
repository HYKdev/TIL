import sys

sys.stdin = open('input.txt')

# 내림차순 정렬 함수
def numbers_sort(args):
    n = len(args)
    for i in range(n):
        for j in range(n-1):
            if args[j] < args[j+1]:
                args[j], args[j+1] = args[j+1], args[j]
    return args

# 단조인지 테스트하는 함수
# 문자열로 바꿔서 인덱스 접근을 쉽게 하고
# 파이썬의 특징인 비교를 이용하여
# True or False를 반환

def danjo_test(num):
    num_str = str(num)
    for i in range(len(num_str)-1, 0, -1):
        if num_str[i] < num_str[i-1]:
            return False
    return True

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers_sort(numbers)
    result = 0

# 2중 반복문을 사용하여 전 범위 탐색
    i = 0
    while i < n:
        for j in range(i+1, n):
            num = numbers[i] * numbers[j]

            if danjo_test(num):
                result = max(result, num)

        i += 1

# 단조로 추가 되는 값이 없으면 -1 반환
    if result == 0:
        result = -1

    print(f'#{tc} {result}')

