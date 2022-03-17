# 치즈
from collections import deque
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# BFS 함수 선언
def BFS():
    q = deque()             # 초기 설정
    visited[0][0] = 1
    q.append([0, 0])
    cnt = -1                # time에 대한 변수를 cnt로 지정

    while q:                    # 치즈녹는게 0이 될 때 까지 도는 반복문
        cnt += 1
        melt_cheese_list = []
        while q:
            i, j = q.pop()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 위로는 BFS 짜는 구문과 같음
                # 아래 조건은 visited를 초기화 하는게 아닌 다음 time에도 활용하기 위해서
                # 조건을 나누고 while문이 끝났을 때 녹은 자리를 활용하기 위한 코드
                # 치즈이면 방문 1 더하고 방문 2이면 녹이는 처리
                # elif는 처음 visited에서 활용하고 내부 빈 공간이 있을 경우 돌고
                # 그 이외에는 방문처리때문에 사용하지 않음
                if 0 <= ni < r and 0 <= nj < c:
                    if matrix[ni][nj] == 1 and visited[ni][nj] < 2:
                        visited[ni][nj] += 1
                        if visited[ni][nj] == 2:
                            melt_cheese_list.append([ni, nj])

                    elif matrix[ni][nj] == 0 and visited[ni][nj] == 0:
                        q.append([ni, nj])
                        visited[ni][nj] = 1

        # 위에서 방문2로 녹인 치즈 자리 리스트를 가져와서 q로 활용
        # visited 재활용하기 위해서 녹인처리와 2번 방문을 1번 방문으로 바꿈
        for i, j in melt_cheese_list:
            matrix[i][j] = 0
            visited[i][j] = 1

        q = melt_cheese_list

    return cnt

# 입력
r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]

print(BFS())