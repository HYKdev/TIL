import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력 받는 곳
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    ans = 0

# 2중 for문을 통한 bubble sort 해서 오름차순 정렬한 후
# 인덱스 -1 값과 0의 값 차이를 출력
    for i in range(N):
        for j in range(N-1):
            if ai[j] > ai[j+1]:
                ai[j], ai[j+1] = ai[j+1], ai[j]
    ans = ai[-1] - ai[0]

    print(f'#{tc} {ans}')


