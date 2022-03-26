# 좌표 정렬하기

from collections import deque

n = int(input())

stack = []
for _ in range(n):
    x, y = map(int, input().split())

    stack.append([x, y])
    
stack.sort()

for i, j in stack:
    print(i, j)   

