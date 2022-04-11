# 게리맨더링

import sys
input = sys.stdin.readline

from collections import deque
from itertools import combinations

def BFS(s):
    q = deque()
    q.append([s[0]])
    while q:
        v = q.popleft()
        for item in graph[v]:
            if not visited[item]:
                visited[item] = 1 + visited[v]
                q.append(item)

n = int(input())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(1, n+1):
    args = list(map(int, input().split()))
    for j in range(1, len(args)):
        graph[i].append(args[j])

min_ans = float('inf')
com_lst = [i for i in range(1, n+1)]
for k in range(1, n//2+1):
    for lst_A in combinations(com_lst, k):
        lst_B = []
        for num in com_lst:
            if num not in lst_A:
                lst_B.append(num)
        
        if BFS(lst_A) and BFS(lst_B):
            result = abs(sum(lst_A)- sum(lst_B))