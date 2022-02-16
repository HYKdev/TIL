import sys

sys.stdin = open('input.txt')

T = int(input())

# 양의 정수를 문자열로 변환하는 함수
def itoa(number):
    rlt = ''

    while True:
        rlt = chr(number % 10 + 48) + rlt

        if number//10 == 0:
            break
        number = number//10
    return rlt

#테스트 케이스 입력
for tc in range(1, T + 1):
    num = int(input())

# 음일 때 - 문자열 추가해서 반환
    if num >= 0:
        result = itoa(num)
    else:
        num = -num
        result = chr(45) + itoa(num)

    print(f'#{tc} {result} {type(result)}')
