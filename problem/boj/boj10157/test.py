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
                ni = i + di[d]
                nj = j + dj[d]
                
                if 0 <= ni < a and 0 <= nj < b and matrix[ni][nj] == 0:
                    i, j = ni, nj
                    break
        return [i+1, j+1]

c, r = map(int, input().split())
k = int(input())

matrix = [[0 for _ in range(r)] for _ in range(c)]

result = check(c, r, k)

if result:
    print(*result)
else:
    print(0)