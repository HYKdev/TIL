# 요세푸스 문제0

from collections import deque

n, k = map(int, input().split())
num_list = deque()
for i in range(1, n+1):
    num_list.append(i)
result = []
print('<', end='')
while num_list:
    for _ in range(k-1):
        item = num_list.popleft()
        num_list.append(item)
    args = num_list.popleft()
    result.append(args)
for i in range(len(result)-1):
    print(result[i], end=', ')
print(result[-1], end='')
print('>')
