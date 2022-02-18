import sys

sys.stdin = open('input.txt')

def sudoku_test(lst):
    count_list = [0 for _ in range(10)]
    for i in range(9):
        count_list[lst[i]] += 1

    for i in range(1, 10):
        if count_list[i] != 1:
            return False
    return True

def square_sudoku_test(lst):

T = int(input())

for tc in range(1, T + 1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    data = list(map(list, zip(*arr)))

    for i in range(9):
        if sudoku_test(arr[i]) and sudoku_test(data[i]):
            rlt = 1
        else:
            rlt = 0

    print(f'#{tc} {rlt}')

