import sys

sys.stdin = open('input.txt')

T = 10


for tc in range(1, T + 1):
    tc_num = int(input())
    tc_list_row = [list(input()) for _ in range(100)]  # 100*100 배열 리스트
    tc_list_col = list(map(list, zip(*tc_list_row)))  # 전치행렬


    row_result = 0  # 모든 행 중에 최대 회문 길이
    for i in range(100):  # 모든 행 0~99
        max_row = 0  # 각 행마다의 최대 회문 길이
        for j in range(100):
            for k in range(j, 100):
                if tc_list_row[i][j:k+1] == tc_list_row[i][j:k+1][::-1]:  # 회문이면
                    row_len = len(tc_list_row[i][j:k+1])  # 회문의 길이
                    if row_len > max_row:
                        max_row = row_len
        if row_result < max_row:  # 행끼리 비교하여 모든 행 중에 최대 회문의 길이 업데이트
            row_result = max_row
    # print(row_result)



    col_result = 0  # 모든 열 중에 최대 회문 길이
    for i in range(100):  # 모든 열 0~99
        max_col = 0  # 각 열마다의 최대 회문 길이
        for j in range(100):
            for k in range(j, 100):
                if tc_list_col[i][j:k+1] == tc_list_col[i][j:k+1][::-1]:  # 회문이면
                    col_len = len(tc_list_col[i][j:k+1])  # 회문의 길이
                    if col_len > max_col:
                        max_col = col_len
        if col_result < max_col:  # 열끼리 비교하여 모든 열 중에 최대 회문의 길이 업데이트
            col_result = max_col



    if row_result > col_result:
        print(f'#{tc_num} {row_result}')
    else:
        print(f'#{tc_num} {col_result}')
    # print(f'#{tc} ')

