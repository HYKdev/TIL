# 쿼드트리

# 쿼드 트리 시작
def quad_tree(arrs, arrs_n):
    # 탐색할 범위가 쿼드 트리인지 체크하기 위해서 변수 초기화 및 합산
    arr_cnt = 0
    for arr in arrs:
        arr_cnt += sum(arr)
    
    # 0으로만 이루어져있으면 0, 1로만 이루어져있으면 1 아니면 분할정복 시작
    if arr_cnt == 0:
        print(0, end='')
    elif arr_cnt == arrs_n*arrs_n:
        print(1, end='')
    else:
        # 분할정복 시작을 괄호 열고 쿼드트리 오른쪽 아래가 끝나면 닫히도록 하고
        # 4방향 분할정복 시작
        
        print('(', end='')
        arrs_temp = [arrs[i][0:arrs_n//2] for i in range(0, arrs_n//2)]
        quad_tree(arrs_temp, arrs_n//2)
        arrs_temp = [arrs[i][arrs_n//2: arrs_n] for i in range(0, arrs_n//2)]
        quad_tree(arrs_temp, arrs_n//2)
        arrs_temp = [arrs[i][0:arrs_n//2] for i in range(arrs_n//2, arrs_n)]
        quad_tree(arrs_temp, arrs_n//2)
        arrs_temp = [arrs[i][arrs_n//2:arrs_n] for i in range(arrs_n//2, arrs_n)]
        quad_tree(arrs_temp, arrs_n//2)
        print(')', end='')

# 입력
n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]

# 함수 호출
quad_tree(matrix, n)