import sys
sys.stdin = open('input.txt')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def DFS(cnt, i, j, word):
    word += matrix[i][j]
    if cnt == 6:
        result.append(word)
        return
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            DFS(cnt+1, ni, nj, word)

T = int(input())
for tc in range(1, T + 1):
    matrix = [list(map(str, input().split())) for _ in range(4)]
    result = []
    for i in range(4):
        for j in range(4):
            DFS(0, i, j, '')

    result = set(result)

    print(f'#{tc} {len(result)}')

