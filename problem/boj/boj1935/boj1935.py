# 후위 표기식

import sys

# 입력 설정
n = int(sys.stdin.readline())
alpabet = [0 for _ in range(26)]
arr = sys.stdin.readline().rstrip()

for i in range(n):
    alpabet[i] = int(sys.stdin.readline())

stack = []
# 입력받은 arr리스트에서 alpabet에 맞는 값을 찾아서 stack에 추가
for token in arr:
    if token.isalpha():
        stack.append(alpabet[ord(token)-ord('A')])

# 연산에 맞는 것을 스택에서 꺼내어 연산 후 저장
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if token == '/':
            stack.append(n1 / n2)
        elif token == '*':
            stack.append(n1 * n2)
        elif token == '+':
            stack.append(n1 + n2)
        elif token == '-':
            stack.append(n1 - n2)

#소수점 둘째자리 까지 출력을 위해서 format함수 사용
print(format(stack[0], ".2f"))