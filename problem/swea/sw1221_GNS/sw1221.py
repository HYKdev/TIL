import sys

sys.stdin = open('input.txt')

def atoi(args):
    change_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(len(change_list)):
        if change_list[i] == args:
            return i

def itoa(args):
    change_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(len(change_list)):
        if i == args:
            return change_list[i]

T = int(input())

for tc in range(1, T + 1):
    test_input = list(input().split())
    data = list(input().split())
    n = int(test_input[1])
    rlt_list = []

    for i in range(n):
        rlt_list.append(atoi(data[i]))

    for i in range(n):
        for j in range(n-1):
            if rlt_list[j] > rlt_list[j+1]:
                rlt_list[j], rlt_list[j+1] = rlt_list[j+1], rlt_list[j]

    rlt = []
    for i in range(n):
       rlt.append(itoa(rlt_list[i]))


    print(f'#{tc}')
    for i in range(n):
        print(rlt[i], end=' ')

