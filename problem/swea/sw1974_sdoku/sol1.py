import sys

sys.stdin = open('input.txt')

def sudoku_test(lst):
    count_list = [0 for _ in range(9)]
    for i in range(9):
        count_list[lst[i]-1] += 1

    for i in range(9):
        if count_list[i] != 1:
            return False
    return True

def square_sudoku_test(lst):
    rlt = 0
    a = [0, 0, 0, 3, 3, 3, 6, 6, 6]
    b = [0, 3, 6, 0, 3, 6, 0, 3, 6]
    k = 0
    count_list = [0 for _ in range(9)]
    for i in range(9):
        count_list[lst[i]-1] += 1

    while k < 9:
        cnt = 0
        for i in range(3):
            for j in range(3):
                cnt += lst[a[k] + i][b[k] + j]
        if cnt != 45:
            rlt = 0
            break
        elif cnt == 45:
            rlt = 1
        k += 1
    return rlt

T = int(input())

for tc in range(1, T + 1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    data = list(map(list, zip(*arr)))
    result = 0

    for i in range(9):
        if sudoku_test(arr[i]) and sudoku_test(data[i]):
            result = 1
        else:
            result = 0
            break
    if square_sudoku_test(arr) == 0:
        result = 0

    print(f'#{tc} {result}')

