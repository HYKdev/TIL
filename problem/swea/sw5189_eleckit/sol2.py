import sys
sys.stdin = open('input.txt')

# DFS 함수
def DFS(e, total):
    global min_energe                       # 글로벌 변수로 둬서 최소 값 체크

    if len(stack) == n:                     # 관리구역을 다 탐색 했으면 종료
        total += matrix[e][0]               # 마지막 관리구역 - 사무실 더해준 다음
        if total < min_energe:              # 최소 값인지 체크 후 맞으면 할당
            min_energe = total
            return

    for k in range(n):                      # 탐색 범위만큼 반복문
        if k not in stack:                  # 아직 탐색한 곳이 아니라면
            stack.append(k)                 # 추가하고 DFS 호출
            DFS(k, total + matrix[e][k])
            stack.pop()                     # 백트래킹을 위해서 pop


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    stack = [0]                 # 사무실이 1번이지만 index로는 0이라서 0 시작
    min_energe = 0              # 최소 에너지를 찾기 위해 matrix전체 합을 기준으로 측정
    for mat in matrix:
        min_energe += sum(mat)

    DFS(0, 0)                   # DFS 호출

    print(f'#{tc} {min_energe}')
