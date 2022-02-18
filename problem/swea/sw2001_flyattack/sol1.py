

T = 2
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

def arr_sum(row, col):
    sum = arr[row][col]
    for k in range(m**2-1):
        sum += arr[row+di[k]][col+dj[k]]
    return sum

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))


    max_sum = 0
    if m == 2:
        for i in range(n-m+1):
            for j in range(n-m+1):
                if max_sum < arr_sum(i, j):
                    max_sum = arr_sum(i, j)


    elif m == 3:
        for i in range(1, n-m+2):
            for j in range(1, n-m+2):
                if max_sum < arr_sum(i, j):
                    max_sum = arr_sum(i, j)


    print(f'#{tc} {max_sum}')

