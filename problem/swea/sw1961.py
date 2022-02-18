# 숫자 배열 회전

# NxN 행렬 90 180 270도 회전

# 90도 180 270도 각각 회전 결과를 보고 인덱스 값 출력

# 출력 함수
# 90도 회전 함수
def rotation_90(array):
    array_len = len(array)
    array_list = []
    for i in range(array_len):
        array_str = ''
        for j in range(array_len-1,-1,-1):
            array_str += array[j][i]
        array_list.append(array_str)
    return array_list

# 180도 회전 함수
def rotation_180(array):
    array_len = len(array)
    array_list = []
    for i in range(array_len-1,-1,-1):
        array_str = ''
        for j in range(array_len-1,-1,-1):
            array_str += array[i][j]
        array_list.append(array_str)
    return array_list

# 270도 회전 함수
def rotation_270(array):
    array_len = len(array)
    array_list = []
    for i in range(array_len-1,-1,-1):
        array_str = ''
        for j in range(array_len):
            array_str += array[j][i]
        array_list.append(array_str)
    return array_list
    
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    n_lists = []
    for i in range(N):
        n_list = list(input().split())
        n_lists.append(n_list)

# 출력 시작
# 90 180 270도를 test_list에 추가
    print(f'#{test_case}')
    test_list = [rotation_90(n_lists)] + [rotation_180(n_lists)] + [rotation_270(n_lists)]

# test_list에 있는 값을 출력예시에 맞게 변환 후 출력
    for i in range(N):
        result = ''
        for j in range(len(test_list)):
            result += test_list[j][i] + ' '
        print(result)