import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    text = input()
    answer = ''
    stack = []

# 입력받은 text를 하나씩 꺼내서 숫자와 문자 비교
    for t in text:
        if t.isdigit():
            answer += t
        else:

# 곱하기 나오면 스택에 쌓인 것과 비교해서 추가
            if t == '*' or t == '/':
                while stack and (stack[-1] == '*'or stack[-1] == '/'):
                    answer += stack.pop()
                stack.append(t)

# 더하기 나오면 스택에 추가
            elif t == '+' or t == '-':
                while stack:
                    answer += stack.pop()
                stack.append(t)

# 스택 확인
    while stack:
        answer += stack.pop()
    print(f'#{tc} {answer}')