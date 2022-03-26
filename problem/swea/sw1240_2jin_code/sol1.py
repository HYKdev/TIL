import sys
sys.stdin = open('input.txt')

# 0~9까지 2진법으로 표현된 암호화 코드와 일치하는 10진수 숫자
P = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

# 입력
T = int(input())
for tc in range(1, T + 1):
    r, c = map(int, input().split())
    matrix = []
    for _ in range(r):
        matrix.append(list(input()))

    # 바코드가 있는 1줄을 받기 위해서 초기화 선언
    arr = []

    # 1이 있는 리스트를 받아서 arr에 할당
    for i in matrix:
        if '1' in i:
            arr = i

    # 0~9까지 모든 숫자들이 1로 끝나서 마지막에 1을 만나면 56개 슬라이싱
    for i in range(1, len(arr)+1):
        if arr[-i] == '1':
            idx = -i
            break
    arr = arr[-55-i:-i+1]

    # 7개씩 8숫자를 결과에 담기
    result = []
    for i in range(0, len(arr), 7):
        test = ''
        for j in range(7):
            test += arr[i+j]

        result.append(P[test])

    # 홀수 짝수를 나눠서 홀수는 3배해서 더하고 짝수는 그냥 더해서
    # 원하는 결과인지 확인
    result_odd = 0
    result_even = 0
    for i in range(len(result)//2):
        result_odd += result[i*2] * 3
        result_even += result[2*i + 1]

    # 원하는 결과면 ans에 담고 아니면 0 반환
    ans = 0
    if (result_even + result_odd) % 10 == 0:
        ans = sum(result)


    print(f'#{tc} {ans}')

