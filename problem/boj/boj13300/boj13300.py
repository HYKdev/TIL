# 방배정

# n, k = 
import sys
from pprint import pprint
sys.stdin = open('input.txt')

n, k = map(int, input().split())
arr = [[0 for _ in range(2)] for _ in range(6)]
for _ in range(n):
    s, y = map(int, input().split())

    arr[y-1][s] += 1

rlt = 0

for i in range(6):
    for j in range(2):
       if 1 <= arr[i][j] <= k:
           rlt += 1
       elif arr[i][j] == 0:
           pass
       elif arr[i][j]%k == 0:
           rlt += arr[i][j]//k
       elif arr[i][j]%k != 0:
           rlt += arr[i][j]//k+1
print(rlt)

