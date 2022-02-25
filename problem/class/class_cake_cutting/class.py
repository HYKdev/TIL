import sys

sys.stdin = open('input.txt')

def total_test(lst):
    total = 0
    for mat in matrix:
        total += sum(mat)
    if total % 4:
        return False
    else:
        return True
def sum_test(lst):
    for i in range(n-1):
        for j in range(n-1):
            left_up, left_down = 0, 0
            right_up, right_down = 0, 0

            for ii in range(i+1):
                for jj in range(j+1):
                    left_up += lst[ii][jj]
            for ii in range(i+1):
                for jj in range(j+1, n):
                    right_up += lst[ii][jj]

            if left_up != right_up:
                continue

            for ii in range(i+1, n):
                for jj in range(j+1):
                    left_down += lst[ii][jj]
            for ii in range(i+1, n):
                for jj in range(j+1, n):
                    right_down += lst[ii][jj]

            if left_down != right_down:
                continue

            if left_up != left_down:
                continue
            return True
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    if not total_test(matrix):
        result = 0
    elif sum_test(matrix):
        result = 1

    print(f'#{tc} {result}')

