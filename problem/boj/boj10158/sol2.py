import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
# 테스트 케이스 입력
    w, h = map(int, input().split())
    j, i = map(int, input().split())
    t = int(input())

# 시간과 현재 포지션 합을 나머지와 몫으로 구분
    j_d, j_p = (t+j)//w, (t+j) % w
    i_d, i_p = (t+i)//h, (t+i) % h

# 몫의 홀,짝으로 if else 구분
    if j_d % 2 == 0:
        pos1 = j_p
    else:
        pos1 = w-j_p

    if i_d % 2 == 0:
        pos0 = i_p
    else:
        pos0 = h-i_p

    print(f'#{tc} {pos1} {pos0}')

