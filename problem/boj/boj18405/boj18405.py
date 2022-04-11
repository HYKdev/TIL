# 경쟁적 전염

from collections import deque

# BFS함수
# args에 좌표가 여러개 임으로 하나씩 꺼내서 append해줌
# (사실 그냥 deque에 바로 넣어도 상관없을 거 같음)
def BFS(args, T):
    q = deque()
    for arg in args:
        q.append(arg)
    # q의 길이만큼 진행시키면 1초가 지난상태라서 아래와 같이
    # 전체 반복문은 T로 돌려서 시간진행 시키고 안에 반복문은 1초단위의 BFS진행
    while T:
        for _ in range(len(q)):
            val, i, j = q.popleft()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n and not matrix[ni][nj]:
                    q.append([val, ni, nj])
                    matrix[ni][nj] = val
        T -= 1

# 방향 벡터 설정
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
# 입력
n, k = map(int , input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

# 1~k까지 좌표를 담기 위해서 초기화
# 행렬 전체를 순회하여 값, 좌표를 받아서 sort하면 값 기준으로 정렬이 되기 때문에 1부터 k까지 순서로 정렬됨
point = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            point.append([matrix[i][j], i, j])

point.sort()

# 몇초후의 좌표의 값을 찾아야 함으로 1~k좌표와 시간을 같이 담아서 BFS전달
BFS(point, s)

# 주어진 값을 인덱스로 나타내면 -1씩 해줘야 해서 1씩 뺌
print(matrix[x-1][y-1])
