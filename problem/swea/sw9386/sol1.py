T = int(input())


for tc in range(1, T + 1):
    n = int(input())
    number_list = list(map(int, input()))+[0]
    max_rlt = 0
    cnt = 0

    for i in range(len(number_list)):
        if number_list[i] == 0:
            if max_rlt < cnt:
                max_rlt = cnt
            cnt = 0
        else:
            cnt += 1

    print(f'#{tc} {max_rlt}')

