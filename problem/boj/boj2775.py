# 부녀회장이 될거야

T = int(input())

matrix = [[0 for _ in range(14)] for _ in range(15)]

for i in range(14):
    matrix[0][i] = i+1

for i in range(1, 15):
    for j in range(14):
        matrix[i][j] = sum(matrix[i-1][:j+1])

for _ in range(T):
    k = int(input())
    n = int(input())
    print(matrix[k][n-1])
