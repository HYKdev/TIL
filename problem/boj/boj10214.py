#Baseball

T = int(input())
cnt_y = 0
cnt_k = 0

for _ in range(T):
    for _ in range(9):
        Y_cnt, K_cnt = map(int,input().split())

        cnt_y += Y_cnt
        cnt_k += K_cnt
    
    if cnt_k > cnt_y:
        print('Korea')
    elif cnt_y > cnt_k:
        print('Yonsei')
    else:
        print('Draw')
