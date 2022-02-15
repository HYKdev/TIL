import sys

sys.stdin = open('input.txt')

# 이진탐색 함수
def binary_search(p, a):
# 시작, 끝 중간, cnt 선언
    start = 1
    end = p
    middle = 0
    cnt = 0
# 찾고자 하는 페이지가 시작 or 끝일 경우 함수 종료
    if a == start or a == end:
        return 0
# while문을 돌려 중간 값을 찾고자 하는 페이지와 비교하여
# 같아 질 때 while 종료
    while True:
        middle = (start + end) // 2
        cnt += 1
        if middle == a:
           break
        elif a > middle:
            start = middle
        else:
            end = middle

    return cnt

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    p, a, b = map(int, input().split())
# 결과 값 초기화
    result = '0'
# 함수를 돌려서 나온 cnt 값을 넣어 비교 후 출력
    a_bi = binary_search(p, a)
    b_bi = binary_search(p, b)

    if a_bi > b_bi:
        result = 'B'
    elif a_bi < b_bi:
        result = 'A'

    print(f'#{tc} {result}')

