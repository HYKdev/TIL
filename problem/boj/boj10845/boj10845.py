# 큐

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
    text = input().split()
    if text[0] == 'push':
        queue.append(text[1])
    elif text[0] == 'pop':
        if len(queue) > 0:
           print(queue.popleft())
        elif len(queue) == 0:
            print(-1)
    elif text[0] == 'size':
        print(len(queue))
    elif text[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif text[0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        elif len(queue) == 0:
            print(-1)
    elif text[0] == 'back':
        if len(queue) > 0:
            print(queue[-1])
        elif len(queue) == 0:
            print(-1)