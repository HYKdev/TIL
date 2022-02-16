import sys

sys.stdin = open('input.txt')

def reverse_function(args):
# 슬라이싱으로 reverse
    ch_1 = args[::-1]

# 리스트의 reverse 메서드를 이용하여 reverse
    ch_2 = list(args)
    ch_2.reverse()
    ch_2 = ''.join(ch_2)

    return [ch_1, ch_2]
# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    ch = input()
    rlt = reverse_function(ch)

    print(f'#{tc} {rlt[0]} // {rlt[1]}')

