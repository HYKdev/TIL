import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    bus_station = [0 for _ in range(5001)]
    for _ in range(n):
        a, b = map(int, input().split())

        for i in range(a, b+1):
            bus_station[i] += 1

    p = int(input())

    print(f'#{tc}', end=" ")
    for _ in range(p):
        c = int(input())
        print(bus_station[c], end=" ")
    print()





