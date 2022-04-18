# 뱀

# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 보드의 크기
n = int(input())

# 사과의 갯수 및 사과 좌표 받기
k = int(input())
apple_info = []
for _ in range(k):
    r, c = map(int, input().split())
    apple_info.append([r-1, c-1])

# 뱀의 정보 받기
L = int(input())
snake_move = {}
for _ in range(L):
    x, c = input().split()
    snake_move[int(x)] = c
    
print(snake_move.keys())

snake = [[0,0]]
snake_direct = 0
time = 0

