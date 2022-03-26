import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

P = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

Q = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(input().strip()))

    idx = 0
    arr = []
    for mat in matrix:
        for i in range(1, m):
            if mat[-i] != '0':
                idx = i
                arr = mat[-13-i:-i+1]
                break
        if len(arr) > 0:
            break
    result = ''

    for num in arr:
        result += P[num]

    for i in range(1, 4):
        if result[-i] == '0':
            result = '0' + result
        elif result[-i] == '1':
            break

    word_list = []
    for i in range(0, 56, 7):
        word = ''
        for j in range(0, 7):
            word += result[i+j]
        word_list.append(Q[word])

    ans_even = 0
    ans_odd = 0
    for i in range(4):
        ans_odd += word_list[2*i]*3
        ans_even += word_list[2*i+1]
    if (ans_odd + ans_even) % 10 == 0:
        ans = sum(word_list)
    else:
        ans = 0

    print(f'#{tc} {ans}')

# 1D 1101
# B1 1011
# 76
# C5
# 88
# D2
# 6E
