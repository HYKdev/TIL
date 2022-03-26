# 색종이 만들기

# 함수에 2차원리스트와 분할정복할 크기 입력
def check(args, args_n):
    # 글로벌 변수로 선언하여 흰색과 파란색 정사각형 갯수 체크
    global ans_blue, ans_white

    # 합산에 이용할 변수 초기화
    color_count = 0

    # 정사각형 합산 후 체크
    for i in range(args_n):
        color_count += sum(args[i])
    
    if color_count == 0:
        ans_white += 1

    elif color_count == args_n * args_n:
        ans_blue += 1

    # 분할 정복 시작
    # 인덱스 슬라이싱을 이용하여 4부분으로 나눈 후 재귀함수 호출
    else:
        args_temp = [args[i][0:args_n//2] for i in range(0,args_n//2)]
        check(args_temp, args_n//2)
        args_temp = [args[i][0:args_n//2] for i in range(args_n//2, args_n)]
        check(args_temp, args_n//2)
        args_temp = [args[i][args_n//2: args_n] for i in range(0,args_n//2)]
        check(args_temp, args_n//2)
        args_temp = [args[i][args_n//2: args_n] for i in range(args_n//2, args_n)]
        check(args_temp, args_n//2)

# 입력
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 갯수 카운트할 변수 초기화
ans_white = 0
ans_blue = 0

# 함수 호출
check(matrix, n)

# 결과 출력
print(ans_white)
print(ans_blue)