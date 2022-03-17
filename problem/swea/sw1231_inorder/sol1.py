import sys
sys.stdin = open('input.txt')

# 중위 표현 배열
def inorder(idx):
    if idx > n:
        return

    if (idx * 2) <= n:
        inorder(idx * 2)
    result.extend(node_list[idx])
    if (idx * 2 + 1) <= n:
        inorder(idx * 2 + 1)

T = 10
for tc in range(1, T + 1):
# node의 값을 인덱스로 활용하여 node리스트에 각 문자를 담음
    n = int(input())
    node_list = ['' for _ in range(n+1)]
    for _ in range(n):
        arr = list(input().split())
        node_list[int(arr[0])] = arr[1]

# 배열에서 꺼낸 문자를 중위 표현으로 각 result에 담고
# ans로 한 문자열로 표현
    result = []
    inorder(1)
    ans = ''
    for text in result:
        ans += text
    print(f'#{tc} {ans}')


