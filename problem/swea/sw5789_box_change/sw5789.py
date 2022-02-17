import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n, q = map(int, input().split())
# n 갯수의 길이만큼 리스트 선언
    numbers = [0 for _ in range(n)]
# i값이 1부터 시작이여서 1~q+1 범위로 잡았고
# l,r도 인덱스가 0부터 시작이여서 l-1로 범위를 잡았습니다.
    for i in range(1, q+1):
        l, r = map(int, input().split())

        for j in range(l-1, r):
            numbers[j] = i

    print(f'#{tc} ', end='')
    print(*numbers)

