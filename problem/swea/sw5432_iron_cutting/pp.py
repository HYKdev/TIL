import sys


sys.stdin = open('input.txt')
T = int(input())
for tc_num in range(1, T+1):
    tc = input()

    stick = 0
    result = 0
    for i in range(len(tc)):
        if tc[i] == '(' and tc[i+1] == '(':
            stick = stick + 1
            result = result + 1
        if tc[i] == ')' and tc[i-1] == ')':
            stick = stick - 1
            # result = result + 1
        if tc[i-1] == '(' and tc[i] == ')':
            if stick > 0 and not tc[i + 1] == ')':
                result = result + stick
            elif stick > 0 and tc[i + 1] == ')':
                result = result + stick - 1
        # if i >= 2 and tc[i] == ')' and tc[i-1] == ')' and tc[i-2] == ')':
        #     result = result - 1
    print(f'#{tc_num} {result}')
