# 종이의 개수
import sys
sys.setrecursionlimit(10**9)

def paper_check(i, j, d):
    global ans 
    pick = matrix[i][j] 
    for it in range(i, i+d): 
        for jt in range(j, j+d): 
            if pick != matrix[it][jt]:
                
                newd = d//3 
                for mi in range(0, 3): 
                    for mj in range(0, 3): 
                        paper_check(i + mi*newd, j + mj*newd, newd) 
                return
    ans[pick] += 1

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0, 0]

paper_check(0, 0, n)

for i in range(-1,2):
    print(ans[i])

