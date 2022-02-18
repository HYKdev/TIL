import sys

sys.stdin = open('input.txt')

T = int(input())

# 가로or세로 기준이 스도쿠가 맞는지 함수
def data_test(lst):
    rlt = 0
    for args in lst:
        cnt = 0
        for i in range(9):
            cnt += args[i]
        if cnt == 45:
            rlt = 1
        else:
            return 0
    return rlt

# 3x3이 스도쿠 조건에 맞는지 함수
def data_square_test(lst):
    rlt = 0
    a = [0, 0, 0, 3, 3, 3, 6, 6, 6]
    b = [0, 3, 6, 0, 3, 6, 0, 3, 6]
    k = 0
    while k < 9:
        cnt = 0
        for i in range(a[k], a[k] + 3):
            for j in range(b[k], b[k] + 3):
                cnt += lst[i][j]
        if cnt != 45:
            rlt = 0
            break
        elif cnt == 45:
            rlt = 1
        k += 1
    return rlt

for tc in range(1, T + 1):
    data1 = []
    for _ in range(9):
        data1.append(list(map(int, input().split())))
# 함수 1개를 돌려 쓰기 위해서 transpose
    data2 = list(map(list, zip(*data1)))
# 결과 초기화
    result = 0
# 스도쿠 조건이 모두 맞으면 1출력 아니면 0
    if data_square_test(data1) and data_test(data1) and data_test(data2):
        result = 1

#출력
    print(f'#{tc} {result}')

