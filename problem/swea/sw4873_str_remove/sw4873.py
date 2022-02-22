import sys

sys.stdin = open('input.txt')

T = int(input())

# 가장 처음 입력 받은 리스트의 0인덱스 값을 넣어주고
# 스택을 쌓아가면서 같으면 빼고 아니면 추가하는 방식
def check(lst):
    lst_count = [lst[0]]
    for i in range(1, len(lst)):
        if len(lst_count) > 0 and lst[i] == lst_count[-1]:
            lst_count.pop()
        else:
            lst_count.append(lst[i])
    return len(lst_count)

for tc in range(1, T + 1):
    arr = list(input())

    print(f'#{tc} {check(arr)}')

