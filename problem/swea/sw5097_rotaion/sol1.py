import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

# 테스트 케이스 입력
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    # deque로 선언한 후 입력 값을 바로 넣기
    q = deque()
    q.extend(list(map(int, input().split())))

    # m번 만큼 popleft하고 append
    for _ in range(m):
        q.append(q.popleft())
    # 출력
    print(f'#{tc} {q.popleft()}')

