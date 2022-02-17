import sys

sys.stdin = open('input.txt')

#테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
# 약수 선언 및 약수 카운트를 추가 할 리스트 선언
    numbers = [2, 3, 5, 7, 11]
    rlt = [0, 0, 0, 0, 0]

# 약수로 나눠지면 cnt 1 증가 아니면 다음 약수로 나눠서 소인수분해
    for i in range(len(numbers)):
        cnt = 0
        while True:
            if n % numbers[i] != 0:
                break
            else:
                n = n//numbers[i]
                cnt += 1
        rlt[i] = cnt

# 출력
    print(f'#{tc} ', end='')
    print(*rlt)

