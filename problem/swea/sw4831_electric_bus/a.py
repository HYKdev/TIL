import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    # 한번 충전으로 이동할 수 있는 정류장 수  k
    # 종점 길이 n
    # 충전기가 설치된 위치 charge
    K , N , M = map(int,input().split())
    charge = list(map(int,input().split()))
    bus_stop = [x for x in range(N)]

    start = 0
    go = K - 0
    cnt = 0
    while True:
        start += K-0
        if start >= N:
            break
        go -= K - 0
        if start in charge:
            if go == 0:
                go = K - 0
                cnt += 1
        else:
            if go == 0:
                if bus_stop[start-1] in charge:
                    go = K - 0
                    cnt += 1
                    start = start - 1
                elif bus_stop[start-2] in charge:
                    go = K - 0
                    cnt += 1
                    start = start -1
                else:
                    cnt = 0


    print(f'#{tc} {cnt}')