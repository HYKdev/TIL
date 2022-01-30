# TGN

N = int(input())

for _ in range(N):
    r, e, c = map(int,input().split())

    ad_sum = e - c
    if ad_sum > r:
        print('advertise')

    elif ad_sum == r:
        print('does not matter')

    else:
        print('do not advertise')
