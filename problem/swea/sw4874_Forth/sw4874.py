import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
# 입력, 스택, 결과 저장할 내용들 선언
    text = input().split()
    stack = []
    result = ''
# 입력받은 문자열을 앞에서 부터 체크
    for token in text:
# 숫자이면 정수형으로 변환 후 push
        if token.isdigit():
            stack.append(int(token))
# .이면 스택에 저장된 값을 결과로 할당
        elif token == '.':
            result = stack.pop()
# . 이외에 +-/*이 들어오면 그에 맞게 계산하고
# 스택에 숫자가 1개만 있다면 error출력
        else:
            p2 = stack.pop()
            if len(stack) < 1:
                result = 'error'
                break
            p1 = stack.pop()
            if token == '*':
                stack.append(p1*p2)
            elif token == '/':
                stack.append(p1//p2)
            elif token == '+':
                stack.append(p1+p2)
            elif token == '-':
                stack.append(p1-p2)
# 다 계산하고 스택에 숫자가 남아있다면 error출력
    if stack:
        result = 'error'

    print(f'#{tc} {result}')
