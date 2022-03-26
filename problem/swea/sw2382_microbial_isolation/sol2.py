import sys
sys.stdin = open('input.txt')

# 벽면에 도착하면 방향 전환 해 줄 함수
def d_change(direct):
    if direct == 1:
        return 2
    elif direct == 2:
        return 1
    elif direct == 3:
        return 4
    elif direct == 4:
        return 3

# 문제 형태에 맞게 벡터 설정 0 상, 하, 좌, 우
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

# 입력
T = int(input())
for tc in range(1, T + 1):
    # matrix크기, time, 미생물 갯수
    n, m, k = map(int, input().split())
    micro_list = [list(map(int, input().split())) for _ in range(k)]
    # 미생물 / 좌표 i, j, 물량, 방향

    # 시간 만큼 반복
    for _ in range(m):
        # 이전 타임의 미생물 진행 상황을 다음 타임에 영향을 안 주기 위해서
        # 방문을 매번 초기화 할 예정
        visited = [[[] for _ in range(n)] for _ in range(n)]
        # micro_list에 있는 리스트 접을 위해서 선언
        # +1을 계속 해주면서 진행 할 예정이라
        micro_num = -1

        for q in micro_list:
            micro_num += 1

            if q[2] > 0:
                ni = q[0] + di[q[3]]
                nj = q[1] + dj[q[3]]
                if ni == 0 or ni == n-1 or nj == 0 or nj == n-1:
                    q[2] = q[2]//2
                    q[3] = d_change(q[3])

                else:
                    if not visited[ni][nj]:
                        visited[ni][nj] = [q[2], q[2], micro_num]
                        # 합산, 최대값, micro 들어온 입력 순번
                    else:
                        if visited[ni][nj][1] > q[2]:
                            visited[ni][nj][0] += q[2]
                            micro_list[visited[ni][nj][2]][2] = visited[ni][nj][0]
                            q[2] = 0

                        else:
                            visited[ni][nj][0] += q[2]
                            visited[ni][nj][1] = q[2]
                            micro_list[visited[ni][nj][2]][2] = 0
                            visited[ni][nj][2] = micro_num
                            q[2] = visited[ni][nj][0]
                q[0] = ni
                q[1] = nj

    total = 0
    for q in micro_list:
        total += q[2]

    print(f'#{tc} {total}')

