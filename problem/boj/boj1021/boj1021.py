# 회전하는 큐

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
q = deque([i for i in range(1,n+1)])
ans = 0
point = 1
for number in arr:
    if q[0] == number:
        q.popleft()
    else:
        index_num = q.index(number)
        if index_num <= n//2:
            q.rotate(-index_num)
            ans += abs(index_num)
        else:
            q.rotate(n-index_num)
            ans += abs(n-index_num)
        q.popleft()
    n -= 1
    
print(ans)