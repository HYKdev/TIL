import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
# 최대 버스 정류장수 만큼 0으로 리스트 만들기
    n = int(input())
    bus_station = [0 for _ in range(5001)]
# a~b까지 입력 받을 때 마다 정류장에 1씩 더하기
    for _ in range(n):
        a, b = map(int, input().split())

        for i in range(a, b+1):
            bus_station[i] += 1

# 출력 범위로 사용
    p = int(input())

# c입력 들어오는 것을 인덱스로 활용
# 위에서 0 인덱스는 자리만 채우는 걸로 활용해서 c-1이 아닌 c그대로 사용
    print(f'#{tc}', end=" ")
    for _ in range(p):
        c = int(input())
        print(bus_station[c], end=" ")
    print()





