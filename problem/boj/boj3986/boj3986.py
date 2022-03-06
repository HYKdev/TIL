# 좋은단어

import sys

n = int(sys.stdin.readline())
result = 0
for _ in range(n):
    arr = sys.stdin.readline().rstrip()
    stack = []

    for token in arr:
        if stack:
            if token == stack[-1]:
                stack.pop()
            else:
                stack.append(token)
        else:
            stack.append(token)
    if not stack:
        result += 1

print(result)