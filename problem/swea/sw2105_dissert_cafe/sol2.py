import sys
sys.stdin = open('input.txt')

def DFS(p_i, p_j, d, dessert_cnt):
    global ans

    for k in range(2):
        tmp_d = (d+k) % 4

        ni = p_i + di[tmp_d]
        nj = p_j + dj[tmp_d]

        if start[0] <= ni < n and 0 <= nj < n:
            if ni == start[0] and nj == start[1]:
                ans = max(ans, dessert_cnt)
                return

            if matrix[ni][nj] not in dessert_list:
                dessert_list.append(matrix[ni][nj])

                DFS(ni, nj, tmp_d, dessert_cnt+1)

                dessert_list.pop()


di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ans = -1

    for i in range(n):
        for j in range(n):
            start = [i, j]
            dessert_list = [matrix[i][j]]
            DFS(i, j, 0, 1)

    print(f'#{tc} {ans}')

