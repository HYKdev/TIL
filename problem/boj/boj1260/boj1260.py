# DFS BFS

import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())

stack = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    stack[s].append(e)
    stack[e].append(s)

