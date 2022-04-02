import sys
sys.stdin = open('input.txt')

# 버스가 갈 수 있는 경우의 수 찾는 함수
# 글로벌 변수 ans를 둬서 충전지 교체가 저장된 ans 보다 크면 최솟값이 아니라서 종료
# 마지막 지점 도착했고 저장된 ans보다 작아야 최솟값이기 때문에 조건에 만족 하면 ans에 저장
# range를 충전된 에너지를 다쓰는 경우부터 1개씩 덜 쓰는 경우를 따져서 change를 체크
# 단 position + i로 넘겨주는 값이 리스트 범위를 넘으면 안되서 조건을 잡아줌

def bus_going(position, change):
    global ans
    if change >= ans:
        return

    if position == len(power_list) - 1 and change < ans:
        ans = change
        return

    power = power_list[position]
    for i in range(power, 0, -1):
        if position + i < len(power_list):
            bus_going(position + i, change + 1)

# 입력
T = int(input())
for tc in range(1, T + 1):
    power_list = list(map(int, input().split()))
    n = power_list[0]
    power_list = power_list[1:] + [0]
    ans = n
    bus_going(0, -1)

    print(f'#{tc} {ans}')

