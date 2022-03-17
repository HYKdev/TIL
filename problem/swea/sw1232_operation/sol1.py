import sys
sys.stdin = open('input.txt')

# -,+,/,* 연산하는 함수
def operation(n1, n2, operate):
    if operate == '+':
        return n1 + n2
    elif operate == '-':
        return n1 - n2
    elif operate == '*':
        return n1 * n2
    elif operate == '/':
        return n1 / n2

# 후위 순회 함수
def postorder(node):
    # 입력값이 n을 넘지 않고 tree에 연산자가 있으면 후위 순회하여 연산
    # 더이상 연산할게 없다면 종료
    if node <= n:
        if type(tree[node][3]) is str:
            left = postorder(tree[node][0])
            right = postorder(tree[node][1])
            tree[node][3] = operation(left, right, tree[node][3])
    return tree[node][3]

# 입력
T = 10
for tc in range(1, T + 1):
    n = int(input())
    # 왼쪽자식, 오른쪽자식, 부모(없어도 이 문제에서는 전혀 상관 없음), idx의 값
    tree = [[0 for _ in range(4)] for _ in range(n+1)]
    # *을 활용하여 0개 이상의 데이터를 리스트로 바로 받음
    for _ in range(n):
        idx, value, *args = input().split()

    # 입력값들을 필요한 type으로 변환
        idx = int(idx)
        if value in '-+*/':
            tree[idx][0] = int(args[0])
            tree[idx][1] = int(args[1])
        else:
            value = int(value)
        tree[idx][3] = value

    # 연산하면서 float형식으로 바껴서 int형으로 다시 변환
    ans = int(postorder(1))

    print(f'#{tc} {ans}')