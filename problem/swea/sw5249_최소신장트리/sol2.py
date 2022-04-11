import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        a, b = b, a
    parents[b] = a

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    parents = {i: i for i in range(V + 1)}
    edges = []
    for __ in range(E):
        a, b, w = map(int, input().split())
        heappush(edges, (w, a, b))

    answer = 0
    while edges:
        w, a, b = heappop(edges)
        if find(a) != find(b):
            union(a, b)
            answer += w
    print(parents)
    print(f'#{tc} {answer}')

