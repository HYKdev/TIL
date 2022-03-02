# 제로
import sys

k = int(sys.stdin.readline())
stack = []
for _ in range(k):
    data = int(sys.stdin.readline())
    
    if data != 0:
        stack.append(data)
    else:
        stack.pop()

print(sum(stack))