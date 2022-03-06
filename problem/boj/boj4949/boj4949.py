# 균형잡힌 세상

def check(lst):
    global result
    stack = []
    for token in lst:
        if token == '(' or token == '[':
            stack.append(token)
        elif token == ')' and len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        elif token == ']' and len(stack) != 0 and stack[-1] == '[':
            stack.pop()
        elif token == ']' or token == ')':
            result = 'no'
            return
    if len(stack) > 0:
        result = 'no'
    return


while True:
    arr = input()
    result = 'yes'
    if arr == ".":
        break

    check(arr)

    print(result)