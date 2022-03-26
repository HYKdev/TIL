import sys
sys.stdin = open('input.txt')

# 백트래킹으로 만들어 볼려고 했으나 오류를 못 찾아서 함수로 만듬
# 들어오는 값을 계속 빼면서 0이되면 출력하고 아니면 None을 반환
def back(args, result, i, ans):

    for j in range(i, 14):
        if args >= 0.5**j:
            result += 0.5**j
            ans.append(1)
            args -= 0.5**j
        else:
            ans.append(0)

        if args == 0.0:
            return ans

# 입력
T = int(input())
for tc in range(1, T + 1):
    number = float(input())
    # 출력에 담을 문자열 초기화
    ans = ''
    # 함수 값을 받아와서 조건문에 따라서 출력에 맞게 변환
    answer = back(number, 0, 1, [])

    if answer == None:
        ans = 'overflow'
    else:
        for a in answer:
           a = str(a)
           ans += a
    # 출력
    print(f'#{tc} {ans}')

