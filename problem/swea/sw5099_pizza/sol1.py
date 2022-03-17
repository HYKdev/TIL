import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

# 테스트 케이스 입력
# visited가 True이면 치즈가 다 녹아서 꺼낸 피자
# pizza_list에 인덱스값과 피자치즈 갯수를 같이 넣어서 인덱스 찾기 쉽게 해결
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    pizza_list = deque()
    arr = list(map(int, input().split()))
    visited = [False for _ in range(m)]
    q = deque()

    for i in range(m):
        pizza_list.append([arr[i], i])

# 처음 화덕에 바로 들어갈 피자 갯수 넣기
    for j in range(n):
        q.append(pizza_list.popleft())

# 반복문을 통해 치즈가 절반 녹은 기준 0이면 추가 아니면 다시 넣기
    while q:
        pizza = q.popleft()
        pizza[0] = pizza[0] // 2
        if pizza[0] != 0:
            q.append([pizza[0], pizza[1]])
        elif pizza[0] == 0 and len(pizza_list):
            q.append(pizza_list.popleft())
            visited[pizza[1]] = True

    print(f'#{tc} {pizza[1]+1}')

