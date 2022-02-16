T = int(input())


for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()+[0]))

    cnt = 1
    max_cnt = 0
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1

    print(f'#{tc} {max_cnt}')

