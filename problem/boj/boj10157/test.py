
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def check(a, b, c):
    global matrix
    i = 0
    j = 0
    d = 0
    cnt = 1

    if a*b < c:
        return 0
    else:
        while True:
            if cnt == c:
                break
            matrix[i][j] = cnt
            cnt += 1
            for k in range(2):
                d = (d+k) % 4
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < b and 0 <= nj < a and matrix[ni][nj] == 0:
                    i, j = ni, nj
                    break
        return [i,j]

c, r = map(int, input().split())
k = int(input())
max_size = max(c, r)
matrix = [[0 for _ in range(max_size)] for _ in range(max_size)]

print(check(c,r,k))