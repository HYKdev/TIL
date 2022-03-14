# 덱

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
d = deque()
for _ in range(n):
    text = input().split()
    
    if text[0] == 'push_front':
        d.appendleft(text[1])
    elif text[0] == 'push_back':
        d.append(text[1])
    elif text[0] == 'pop_front':
        if len(d) > 0:
            print(d.popleft())
        else:
            print(-1)
    elif text[0] == 'pop_back':
        if len(d) > 0:
            print(d.pop())
        else:
            print(-1)
    elif text[0] == 'size':
        print(len(d))
    elif text[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif text[0] == 'front':
        if len(d) > 0:
            print(d[0])
        else:
            print(-1)
    elif text[0] == 'back':
        if len(d) > 0:
            print(d[-1])
        else:
            print(-1)