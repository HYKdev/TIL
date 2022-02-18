import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

# 카운팅 sort
    count = [0 for _ in range(n+1)]
    for i in range(len(arr)):
        count[arr[i]] = 1

# 원하는 출력대로 하기 위해서 변형
    print(f'#{tc} ', end='')
    for i in range(1, n+1):
        if count[i] == 0:
            print(i, end=' ')
    print()
