# 오큰수

import sys
input = sys.stdin.readline

def check(lst):
    result = [-1 for _ in range(n)]
    stack = [0]
    for i in range(1, n):
        while stack and lst[stack[-1]] < lst[i]:
            result[stack.pop()] = lst[i]
        stack.append(i)
    return result

n = int( input() )
arr = list(map(int, input().split()))


print(*check(arr))
