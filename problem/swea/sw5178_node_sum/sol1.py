import sys
sys.stdin = open('input.txt')

# 입력
T = int(input())
for tc in range(1, T + 1):
    n, m, node_number = map(int, input().split())
    tree = [0 for _ in range(n+1)]

    for _ in range(m):
        child_node, child_node_num = map(int, input().split())
        tree[child_node] = child_node_num

# node 갯수가 짝수이면 자식노드 왼쪽만 생기는 경우가 발생해서 append로 추가해줌
    if n % 2 == 0:
        tree.append(0)

# 순회를 통해 부모의 값이 비어있는 곳을 자식의 합으로 채워 넣음
    for i in range((n//2)*2, 1, -2):
        tree[i//2] = tree[i] + tree[i+1]
    print(f'#{tc} {tree[node_number]}')

