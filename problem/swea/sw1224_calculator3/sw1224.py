import sys

sys.stdin = open('input.txt')

def calculate(post_ex):
    n = len(post_ex)
    stack = []
    for i in range(n):
# 숫자면 stack
        if post_ex[i].isdigit():
            stack.append(post_ex[i])
        else:

# 곱하기 나오면 두개빼서 곱하고 다시 넣음
            if post_ex[i] == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))

# 더하기 나오면 두개 빼서 더하고 다시 넣음
            elif post_ex[i] == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            else:
                stack.pop()
    return stack[0]

T = 10
for tc in range(1, T + 1):
# isp, icp 선언
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 0, '(': 0}
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 0, '(': 3}
    n = int(input())
    text = list(input())
    stack = []
    answer = ''
# 입력받은 문자열을 하나씩 비교하여 스택 or answer에 저장
    for token in text:
        if token.isdigit():
           answer += token
        else:
# 닫힌 괄호가 나오면 스택에서 pop하고 ( 괄호까지 pop
            if token == ')':
                while stack and (stack[-1] != '('):
                    answer += stack.pop()
                stack.pop()
# 닫힌 괄호를 제외한 나머지 값이 들어오면 icp, isp비교하여 pop과 스택에 추가
            else:
                while stack and icp[token] <= isp[stack[-1]]:
                    answer += stack.pop()
                stack.append(token)
# 스택에 남은게 있다면 그만큼 answer에 추가
    while stack:
        answer += stack.pop()

    print(f'#{tc} {calculate(answer)}')