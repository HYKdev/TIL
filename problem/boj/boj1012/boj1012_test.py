import sys
sys.setrecursionlimit(10**7)

def dfs(si, sj):
    global ans
    global check

    if check:
        return

    if (0>si) or (N<=si) or (0>sj) or (M<=sj) or arr[si][sj]==0:
        return

    arr[si][sj] = 0

    dfs(si-1, sj)
    dfs(si+1, sj)
    dfs(si, sj-1)
    dfs(si, sj+1)

    if check != True:
        ans += 1
    check = True
    return

T = int(input())

for test_case in range(T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1

    ans = 0


    for i in range(M):
        for j in range(N):
            check = False
            dfs(i, j)
    print(ans)