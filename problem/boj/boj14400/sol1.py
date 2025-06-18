# 영선이는 이번에 편의점으로 창업을 하려고 계획 중이다.
# 이번 창업을 위해 많은 준비를 하고 있는데,
# 아직 편의점을 세울 위치를 결정을 하지 못했다.
# 영선이는 미리 시장조사를 하여, 주요 고객들이 어느 위치에 존재하는지 파악을 하였고,
# 모든 고객들의 거리의 합을 최소로 하려한다. 두 위치의 거리는 |x1-x2|+|y1-y2|로 정의한다.

# n명의 주요 고객들의 위치 (xi,yi)이 주어질 때,
# 모든 고객들의 거리 합을 최소로 하는 위치에 편의점을 세울 때, 그 최소 거리 합을 출력하시오.

# 5 
# 2 2
# 3 4
# 5 6 
# 1 9
# -2 -8

import sys

n = int(input())

x_list = []
y_list = []
for _ in range(n):
    item_x, item_y = map(int, sys.stdin.readline().rstrip().split())
    x_list.append(item_x)
    y_list.append(item_y)

x_list.sort()
y_list.sort()

point_x = x_list[(n-1)//2]
point_y = y_list[(n-1)//2]

total = 0
for i in range(n):
    total += abs(point_x - x_list[i]) + abs(point_y - y_list[i])

print(total)
