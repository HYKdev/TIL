# 괄호

import sys

# lst를 체크해서 괄호 조건이 맞으면 yes 아니면 종료하는 함수
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

#입력
n= int(sys.stdin.readline())


for _ in range(n):
    arr = sys.stdin.readline()
    result = 'NO'
    check(arr)
    print(result)