import sys

sys.stdin = open('input.txt')


# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    data = list(input())

# 현재 막대 라인과 나눠진 막대 갯수 선언
    iron = 0
    iron_cnt = 0

# 처음부터 마지막 문자열을 비교하여
# 막대와 라인 추가 / 잘릴 때 막대 추가 / 라인 제거 조건을 각각 두어 계산
    for i in range(len(data)-1):
        if data[i] == '(' and data[i+1] == '(':
            iron += 1
            iron_cnt += 1
        if iron > 0 and data[i] == '(' and data[i+1] == ')':
            iron_cnt += iron
        if data[i] == ')' and data[i+1] == ')':
            iron -= 1

# 출력
    print(f'#{tc} {iron_cnt}')

