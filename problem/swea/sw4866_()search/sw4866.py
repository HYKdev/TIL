import sys

sys.stdin = open('input.txt')

T = int(input())
# 괄호 테스트 함수
def check(lst):
# 받은 리스트 길이와 스택 쌓을 리스트 선언
    n = len(lst)
    lst_count = []
# 입력받은 모든 문자열 탐색
# 열린 괄호가 들어오면 추가하고
# 닫힌 괄호는 조건을 나눠서 pop할지 말지 결정
# 탐색이 끝나면 남은 괄호가 있는지 확인하여 함수 종료
    for i in range(n):
        if lst[i] == '{' or lst[i] == '(':
            lst_count.append(lst[i])
        elif lst[i] == '}':
            if len(lst_count) > 0 and lst_count[-1] == '{':
                lst_count.pop()
            else:
                return False
        elif lst[i] == ')':
            if len(lst_count) > 0 and lst_count[-1] == '(':
                lst_count.pop()
            else:
                return False
    if len(lst_count) > 0:
        return False
    return True

# 테스트 케이스 입력
for tc in range(1, T + 1):
# 문자열로 받아서 괄호테스트를 할 예정
    arr = input()
    rlt = 0
    if check(arr):
        rlt = 1

    print(f'#{tc} {rlt}')

