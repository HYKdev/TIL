import sys

sys.stdin = open('input.txt')

T = 10
# 회문 함수
# 원본 리스트와 뒤집은 리스트를 비교하여 같다면 길이 출력
def palindrome_list(args):
# 함수의 입출력 선언
    m = len(args)
    max_pal = 0
# 모든 경우의 수를 보기 위해서 2중 for문
    for i in range(m):
# 기준점이 바뀔 때 마다 결과값과 리스트 초기화
        rlt = 0
        pal_lst = []
        for j in range(i, m):
            pal_lst.append(args[j])
            if pal_lst[::] == pal_lst[::-1]:
                rlt = len(pal_lst)
# 최대값 비교
        if rlt > max_pal:
            max_pal = rlt
    return max_pal

#테스트 케이스 입력
for tc in range(1, T + 1):
    n = int(input())
    data = []
    for _ in range(100):
        data.append(list(input()))
# transpose
    data2 = list(map(list, zip(*data)))
    rlt = 0

# 최대값 비교
    for lst in data:
        if rlt < palindrome_list(lst):
            rlt = palindrome_list(lst)

    for lst in data2:
        if rlt < palindrome_list(lst):
            rlt = palindrome_list(lst)

    print(f'#{tc} {rlt}')

