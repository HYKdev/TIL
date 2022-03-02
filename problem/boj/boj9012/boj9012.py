# 괄호

import sys

n= int(sys.stdin.readline())
def check(lst):
    global result
    stack = []
    for token in lst:
        if token == '(':
            stack.append(token)
        elif token == ')':
            if len(stack) == 0:
                return
            elif stack[-1] == '(':
                stack.pop()
    if len(stack) == 0:
        result = 'YES'
    return

for _ in range(n):
    arr = sys.stdin.readline()
    result = 'NO'
    check(arr)
    print(result)