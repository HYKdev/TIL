import sys

sys.stdin = open('input.txt')

# 가위바위보 결과 출력
def RCP_check(num1, num2):
    left, right = arr[num1-1], arr[num2-1]

# 가위바위보 승리하면 이긴 사람 인덱스 출력
    if left == right:
        return num1
    elif left == 1:
        if right == 3:
            return num1
        elif right == 2:
            return num2
    elif left == 2:
        if right == 1:
            return num1
        elif right == 3:
            return num2
    elif left == 3:
        if right == 2:
            return num1
        elif right == 1:
            return num2

# 가위바위보 인원 나누기
def RCP(low, high):
    if low == high:
        return low
    else:
        mid = (low + high) // 2
        left = RCP(low, mid)
        right = RCP(mid+1, high)
        return RCP_check(left, right)

#테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = RCP(1, n)

    print(f'#{tc} {result}')

