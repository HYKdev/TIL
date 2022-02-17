import sys

sys.stdin = open('input.txt')


# 테스트 케이스 입력 받기
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input()))
    
# 출력에 들어갈 값 카드번호와 갯수를 리스트 2개로 나눠서 저장
# 입력 값에 대응하는 카운트 리스트 생성
    ans = [0, 0]
    greed = [0] * 10

    for number in numbers:
        greed[number] += 1

# 최대 값과 그 인덱스 값을 ans 리스트에 각각 저장
    for i in range(10):
        if greed[i] >= ans[1]:
            ans[0] = i
            ans[1] = greed[i]

    print(f'#{tc} {ans[0]} {ans[1]}')