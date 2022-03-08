# 후위 표기식
import sys

isp = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 0, '(': 0}
icp = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 0, '(': 3}

input = sys.stdin.readline

text = input().rstrip()
answer= ''
stack = []

for token in text:
    if token.isalpha():
        answer += token
    
    else:
        if token == ')':
            while stack and (stack[-1] != '('):
                answer += stack.pop()
            stack.pop()

        else:
            while stack and icp[token] <= isp[stack[-1]]:
                answer += stack.pop()
            stack.append(token)
while stack:
    answer += stack.pop()

print(answer)