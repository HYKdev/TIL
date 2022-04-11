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
    apple_info.append([r, c])

# 뱀의 정보 받기
L = int(input())
snake_move_time = []
snake_move = {}
for _ in range(L):
    x, c = input().split()
    snake_move_time.append(int(x))
    

snake = [[1,1]]
snake_direct = 0
time = 0
while True:
    if time in snake_move_time:
