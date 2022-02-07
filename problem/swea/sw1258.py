# 행렬
# 빈용기 0
# 화학물질 1~9
# 000 포지션

# 입력 구간
T = int(input())

for test_case in range(T):
    n = int(input())
    data = []
    data.append([0 for _ in range(n+2)])
    for _ in range(n):
        data.append([0]+list(map(int,input().split()))+[0])
    data.append([0 for _ in range(n+2)])

# 꼭지점 4 곳 인덱스 리스트
    p1 = []
    p2 = []
    p3 = []
    p4 = []

    for i in range(n+2):
        for j in range(n+2):
            if data[i][j] !=0 and data[i][j-1] == 0 and data[i-1][j] == 0:
                p1 += [i,j]
            if data[i][j] !=0 and data[i][j+1] == 0 and data[i-1][j] == 0:
                p2 += [i,j]
            if data[i][j] !=0 and data[i][j-1] == 0 and data[i+1][j] == 0:
                p3 += [i,j]
            if data[i][j] !=0 and data[i][j+1] == 0 and data[i+1][j] == 0:
                p4 += [i,j]