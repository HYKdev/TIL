import sys

sys.stdin = open('input.txt')

# 방번호에 따른 인덱스 조정하는 함수
def even_odd(args):
    if args%2 == 0:
        return args//2-1
    else:
        return args//2
# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
# 방을 400개가 아닌 200개로 잡은 이유는 1,2를 1개의 방으로 봐야함
    arr = [0 for _ in range(200)]
    for _ in range(n):
        a, b = map(int, input().split())
# a,b 중에 큰 값이 앞에 있으면 스위칭
        if a > b:
            a, b = b, a
        a = even_odd(a)
        b = even_odd(b)

# 동선 겹치는지 테스트
        for i in range(a, b+1):
            arr[i] += 1

    rlt = max(arr)

    print(f'#{tc} {rlt}')