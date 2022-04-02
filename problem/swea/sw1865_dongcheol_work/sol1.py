import sys
sys.stdin = open('input.txt')

# DFS+백트래킹
# 글로벌 변수로 ans 둬서 작거나 같으면 종료되게 설정
# 마지막까지 가지치기를 했고 최대값 갱신을 할 수 있다면 ans저장 후 종료
# 방문 하지 않았다면 다음 DFS호출 및 백트래킹 하는 과정을 반복
def DFS(cnt, total):
    global ans
    if ans >= total:
        return

    if cnt == n and ans < total:
        ans = total
        return

    for k in range(n):
        if not visited[k]:
            visited[k] = 1
            cnt += 1
            DFS(cnt, total * matrix[cnt-1][k] / 100)
            cnt -= 1
            visited[k] = 0

# 입력
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    ans = 0

    DFS(0, 1)
    # 소수점 6자리까지 표현하기 위해서 나눠서 사용
    print(f'#{tc}', end = ' ')
    print("{:.6f}".format(ans*100))

