import sys
sys.stdin = open('input.txt')

"""
트리 순회 : root 노드를 기준으로 생각하면 쉽습니다.
1. 전위 순회 (preorder)  
"""
def preorder(node):
    """
    전위 순회 하는 함수입니다.
    root => 왼쪽 서브트리의 root => 오른쪽 서브트리의 root
    :param node: node의 번호이자 현재 방문하는 노드
    :return: 없습니다.
    """
    if node:
        # 1. root 방문
        print(node, end=' ')
        # 2. 왼쪽 방문
        preorder(tree[node][0])
        # 3. 오른쪽 방문
        preorder(tree[node][1])

def inorder(node):
    """
    중위 순회 함수입니다.
    왼쪽 서브트리의 root => root => 오른쪽 서브트리의 root

    :param node: 현재 방문하는 노드
    :return: 없습니다
    """
    if node:
        inorder(tree[node][0])
        print(node, end=' ')
        inorder(tree[node][1])

def postorder(node):
    """
    후위 순회 함수입니다.
    왼쪽 서브트리의 root => 오른쪽 서브트리의 root => root

    :param node: 현재 방문하는 노드
    :return: 없습니다
    """
    if node:
        inorder(tree[node][0])
        inorder(tree[node][1])
        print(node, end=' ')


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    edges = list(map(int, input().split()))

    tree = [[0 for _ in range(3)] for _ in range(n+1)]

    for i in range(0, len(edges)-1, 2):
        parent_node = edges[i]
        child_node = edges[i+1]

        if tree[parent_node][0] == 0:
            tree[parent_node][0] = child_node

        else:
            tree[parent_node][1] = child_node

        tree[child_node][2] = parent_node

    # for a in tree:
    #     print(a)

    print('===전위 순회===')
    start_node = 1
    preorder(start_node)
    print()
    print('===전위 순회 끝===')

    print('===중위 순회===')
    start_node = 1
    inorder(start_node)
    print()
    print('===중위 순회 끝===')

    print('===후위 순회===')
    start_node = 1
    postorder(start_node)
    print()
    print('===후위 순회 끝===')


    # graph = [[] for _ in range(n)]
    #
    # graph[1].extend([2, 3])
    # graph[2].extend([4])
    # graph[3].extend([5, 6])
    # graph[4].extend([7])
    # graph[5].extend([8, 9])
    # graph[6].extend([10, 11])
    # graph[7].extend([12])
    # graph[11].extend([13])
    # for i in range(len(graph)):
    #     for j in range(len(graph[i])):
    #         print(i, graph[i][j], end=' ')