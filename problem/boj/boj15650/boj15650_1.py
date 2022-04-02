def dfs(start):

    # 종료 조건 s에 2개가 담기면 프린트 하고 종료
    if len(s) == m:
        print(*s)
        return

    # start지점부터 for문을 돌려야 12 13 14 이런 순서로 돌릴 수 있음
    # dfs가 return하면 pop만나고 for문 반복
    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

n, m = map(int, input().split())
s = []

dfs(1)