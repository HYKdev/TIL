# 스택
import sys

#입력
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    data = sys.stdin.readline().split()

# push, pop, size, empty, top에 대한 각 조건에 대해 맞는 출력 조건문
    if data[0] == 'push':
        arr.append(data[1])
    elif data[0] == 'pop':
        if len(arr) > 0:
            print(arr.pop())
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(arr))
    elif data[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == 'top':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
