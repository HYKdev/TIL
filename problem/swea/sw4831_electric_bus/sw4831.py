import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

# c_s 설치된 정류장 번호 charge_station
# b_e 최대 정류장 거쳐간 수 bus_energy
# l_s 종점 번호 last_station
for tc in range(1, T + 1):
    b_e, l_s, c_s = map(int, input().split())
    numbers = list(map(int, input().split()))

# bus_station 다 0으로 넣고 카운팅 할 리스트 만들기
    b_s = [0 for _ in range(l_s+1)]

# bus_station 충전기가 있으면 1 없으면 0으로 만든 리스트
    for number in numbers:
        b_s[number] += 1

# bus_position 현재 idx
# cnt 충전 횟수
    b_p = 0
    cnt = 0

# 버스의 자리가 마지막 정거장보다 넘어가면 종료
    while True:
        b_p += b_e
        if b_p >= l_s:
            break

# 버스 에너지를 다 쓰고 자리가 0이면
# 그 이전 인덱스로 가서 1을 찾는다.
# 1을 찾을 경우 for문을 나온다.
        if b_s[b_p] == 0:
            for i in range(b_p, b_p-b_e, -1):
                if b_s[i] == 1:
                    b_p = i
                    cnt += 1
                    break
# 에너지 범위안에 1이 없다면 0을 반환
            else:
                cnt = 0
                break
# 에너지 사용 다 했을 때 자리가 충전기 있다면 cnt 1추가
        else:
            cnt += 1

    print(f'#{tc} {cnt}')

