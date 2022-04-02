import sys

sys.stdin = open('input.txt')

# 전위 순회
def preorder(node):
    if node:
        print(node, end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])

# 중위 순회
def inorder(node):
    if node:
        inorder(tree[node][0])
        print(node, end=' ')
        inorder(tree[node][1])

# 후위 순회
def postorder(node):
    if node:
        inorder(tree[node][0])
        inorder(tree[node][1])
        print(node, end=' ')

# 입력
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    edges = list(map(int, input().split()))
    # tree 초기화
    tree = [[0 for _ in range(3)] for _ in range(n + 1)]

    # 입력 받은 edge를 tree에 담기 위해서 부모 노드 자식노드로 나눠서
    # 자식노드의 왼쪽부터 우선적으로 담고 자식노드에 부모노드가 누구인지 담기
    for i in range(0, len(edges) - 1, 2):
        parent_node = edges[i]
        child_node = edges[i + 1]

        if tree[parent_node][0] == 0:
            tree[parent_node][0] = child_node
        else:
            tree[parent_node][1] = child_node

        tree[child_node][2] = parent_node

    # 전위 중위 후위 순으로 해서 1을 시작으로 순회 시작
    print('전위 순회 : ', end='')
    start_node = 1
    preorder(start_node)
    print()

    print('중위 순회 : ', end='')
    start_node = 1
    inorder(start_node)
    print()

    print('후위 순회 : ', end='')
    start_node = 1
    postorder(start_node)
    print()