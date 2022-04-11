import sys
sys.stdin = open('input.txt')

def DFS():


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    visited = [[0 for _ in range(n)] for _ in range(n)]
    print(f'#{tc} ')

