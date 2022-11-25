#체스판 만들기

N, M = map(int ,input().split())

matrix = []
for i in range(N):
    matrix.append(list(input()))

main_cnt = float('inf')

for i in range(N-7):
    for j in range(M-7):
        cnt = 0   
        if matrix[i][j] == 'W':
            for ii in range(8):
                for jj in range(8):
                    if (ii + jj)%2 == 0 and matrix[i+ii][j+jj] == 'B':
                        cnt += 1
                    if (ii + jj)%2 != 0 and matrix[i+ii][j+jj] == 'W':
                        cnt += 1

        if matrix[i][j] == 'B':
            for ii in range(8):
                for jj in range(8):
                    if (ii + jj)%2 == 0 and matrix[i+ii][j+jj] == 'W':
                        cnt += 1
                    if (ii + jj)%2 != 0 and matrix[i+ii][j+jj] == 'B':
                        cnt += 1

        if cnt > 32:
            cnt = 64 - cnt
            
        if main_cnt > cnt:
            main_cnt = cnt
        
        


print(main_cnt)