# 3의 배수

import sys
input = sys.stdin.readline

def check(args, cnt):
    total = 0
    for number in args:
        total += int(number)
    cnt += 1
    args = int(args)
    if args//10 == 0 and total%3 == 0:
        print(cnt-1)
        print('YES')
        return 
    elif args//10 == 0 and total%3 != 0:
        print(cnt-1)
        print('NO')
        return
    total = str(total)
    check(total, cnt)

x = input().rstrip()


check(x, 0)
