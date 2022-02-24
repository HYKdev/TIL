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

# 테스트 케이스 입력
for tc in range(1, T + 1):
    n = int(input())
    text = input()
    answer = ''
    stack = []

# 입력받은 text를 하나씩 꺼내서 숫자와 문자 비교
    for t in text:
        if t.isalnum():
            answer += t
        else:

# 곱하기 나오면 스택에 쌓인 것과 비교해서 추가
            if t == '*':
                while stack and (stack[-1] == '*'):
                    answer += stack.pop()
                stack.append(t)

# 더하기 나오면 스택에 추가
            elif t == '+':
                while stack:
                    answer += stack.pop()
                stack.append(t)

# 스택 확인
    while stack:
        answer += stack.pop()
    print(answer)
    print(f'#{tc} {calculate(answer)}')

