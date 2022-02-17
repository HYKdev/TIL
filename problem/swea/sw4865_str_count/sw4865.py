import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())
# 각 문자열 길이 선언
    n = len(str1)
    m = len(str2)
# 최댓값 초기화
    max_str = 0

# str1과 str2를 비교
    for str1_str in str1:
        cnt = 0
        for str2_str in str2:
            if str1_str == str2_str:
                cnt += 1
# 최댓값 비교
        if max_str < cnt:
            max_str = cnt

# 출력
    print(f'#{tc} {max_str}')

