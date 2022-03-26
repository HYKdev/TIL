import sys
sys.stdin = open('input.txt')

hexa_code = {
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

password_code = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = sorted(list(set([input()[:m] for _ in range(n)])))
    answer = 0
    visited = []
    matrix.pop(0)
    matrix_len = len(matrix)

    for j in range(matrix_len):
        word = ''
        for i in range(len(matrix[j])):
            word += hexa_code[matrix[j][i]]
        word = word.rstrip("0")

        dec_num_list = []
        n1 = n2 = n3 = n4 = 0
        for i in range(len(word)-1, -1, -1):
            if word[i] == '1' and n3 == 0:
                n4 += 1
            elif word[i] == '0' and n2 == 0:
                n3 += 1
            elif word[i] == '1' and n1 == 0:
                n2 += 1
            elif word[i] == '0':
                if word[i-1] == '1':
                    n = min(n2, n3, n4)
                    dec_num_list.append((password_code[n2//n, n3//n, n4//n]))
                    n2 = n3 = n4 = 0
                    if len(dec_num_list) == 8:
                        ans_odd = (dec_num_list[1] + dec_num_list[3] + dec_num_list[5] + dec_num_list[7]) * 3
                        ans_even = dec_num_list[0] + dec_num_list[2] + dec_num_list[4] + dec_num_list[6]
                        if not (ans_even + ans_odd) % 10:
                            if dec_num_list not in visited:
                                answer += sum(dec_num_list)
                                visited.append(dec_num_list)
                        dec_num_list = []

    print(f'#{tc} {answer}')

