import sys

sys.stdin = open('input.txt')

# 페이퍼 dp
# 10일때 1개 20일떄 3개 30일때 5개 40일때 11개 50일때 21개
# a(n) = a(n-1) + 2 * a(n-2)
# 막대기 1개와 + 막대기2개(가로) + 막대기 큰거 1개를 조합한 방법
def paper(number):
    global memo
    if number >= 3 and len(memo) <= number:
        memo.append(paper(number-1) + 2 * paper(number-2))
    return memo[number]

#테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
# 결과 값 초기화
    rlt = 0
# 인덱스 활용하기 위해서 10으로 나눈 나머지 이용
    num = n//10
# memo 리스트를 만들어 dp 값을 저장할 예정
    memo = [0, 1, 3]
    rlt = paper(num)

    print(f'#{tc} {rlt}')

