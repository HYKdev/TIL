# 프린터 큐

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())



for _ in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque(arr)

    
