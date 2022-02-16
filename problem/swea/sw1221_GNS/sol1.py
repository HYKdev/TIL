import sys

sys.stdin = open('input.txt')


#테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
# 0~9까지를 나타내는 문자열 리스트 선언
    number_alpha = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    test_case = list(input().split())
    data_list = list(input().split())

# 결과 출력할 빈 리스트 선언
    rlt = []

# 입력 받은 리스트를 0~9까지 나타내는 문자열 리스트와 비교하여
# 빈 리스트에 추가
    for i in range(len(number_alpha)):
        for j in data_list:
            if number_alpha[i] == j:
                rlt.append(j)

    print(f'#{tc}')
    print(*rlt)
