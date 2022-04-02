import sys
sys.stdin = open('input.txt')

# 최소 생산 비용 찾기 함수
# min_ans를 글로벌 변수로 두고 끝까지 다 안 더해도 total이 min_ans보다 높으면 백트래킹
# 생산비용 합산 다 했고 최소값 갱신할 수 있으면 min_ans 담기
# dfs처럼 깊이 우선 탐색 시작
def min_price(cnt, total):
    global min_ans
    if total > min_ans:
        return

    if cnt == n and min_ans > total:
        min_ans = total
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            min_price(cnt, total + matrix[cnt-1][i])
            cnt -= 1
            visited[i] = 0

# 입력
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    min_ans = float('inf')
    min_price(0, 0)

    print(f'#{tc} {min_ans}')

