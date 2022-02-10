# 행렬
# 빈용기 0
# 화학물질 1~9
# 000 포지션

# 가로 길이 재는 함수
def width(args):
    cnt = 1
    dx = args[1]
    while True:
        dx += 1
        if dx >= n+1 : break
        if data[args[0]][dx]: cnt += 1
        else: break
    return cnt

# 세로 길이 재는 함수
def height(args):
    cnt = 1
    dy = args[0]
    while True:
        dy += 1
        if dy >= n+1: break
        if data[dy][args[1]]: cnt += 1
        else: break
    return cnt

# 입력 구간
T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    data = []
    data.append([0 for _ in range(n+2)])
    for _ in range(n):
        data.append([0]+list(map(int,input().split()))+[0])
    data.append([0 for _ in range(n+2)])

# 꼭지점 4 곳 중 왼쪽 위 인덱스 리스트 
    p_top = []

# 꼭지점 4곳 중 왼쪽 위의 인덱스 값 받아오기
    for i in range(n+2):
        for j in range(n+2):
            if data[i][j] !=0 and data[i][j-1] == 0 and data[i-1][j] == 0:
                p_top.append([i,j])

# 인덱스 값을 통해서 가로 세로 길이 및 넓이를 리스트로 만든 후 sort 정렬
    answer_list = []
    for p_p in p_top:
        answer_list.append([height(p_p),width(p_p),width(p_p)*height(p_p)])

    answer_list = sorted(answer_list, key=lambda x: (x[2], x[0]))

# 출력
    print(f'#{test_case} {len(answer_list)}', end =' ')
    for a0, a1, _ in answer_list:
        print(f'{a0} {a1}', end=' ')
    print()



























#             if data[i][j] !=0 and data[i][j+1] == 0 and data[i-1][j] == 0:
#                 p_top.append([i,j])
#             if data[i][j] !=0 and data[i][j-1] == 0 and data[i+1][j] == 0:
#                 p_bottom.append([i,j])
#             if data[i][j] !=0 and data[i][j+1] == 0 and data[i+1][j] == 0:
#                 p_bottom.append([i,j])

#     print(p_top)
#     print(p_bottom)
#     p_list = []

# # 탑 리스트에 있는 연속된 2개의 [i][1] 값의 차이가 가로
# # 탑의 [i][1] 값과 바텀의 [j][1]을 앞에서부터 비교하여 처음 값이 같은 [j][0]를 통해 세로
# # 를 구하여 넓이와 가로,세로를 리스트 or 딕셔너리로 만든 후 sort 후 출력

#     for i in range(0,len(p_top),2):
#         p_width = p_top[i+1][1]-p_top[i][0]+1
#         a = p_top[i][1]
#         b = p_top[i][0]
#         cnt =0
#         while cnt != 1:
#             j = 0
#             if a == p_bottom[j][1]:
#                 p_vertical = p_bottom[j][0]-b+1
#                 p_bottom[j] = [0,0]
#                 p_bottom[j+1] = [0,0]
#                 p_area = p_width * p_vertical
#                 p_list.append([p_area, p_width, p_vertical])
#                 cnt += 1
#             else:
#                 j = j + 2