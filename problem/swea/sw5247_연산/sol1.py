import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(number):
    q = deque()
    q.append(number)
    while q:
        i = q.popleft()
        if i == m:
            return distance[i]

        for ni in [i+1, i-1, i * 2, i-10]:
            if 0 <= ni <= 1000000 and not distance[ni]:
                distance[ni] = distance[i] + 1
                q.append(ni)

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    distance = [0 for _ in range(1000000+1)]
    print(f'#{tc} {BFS(n)}')

