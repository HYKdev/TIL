import sys
sys.stdin = open('input.txt')

# 중위 표현으로 result에 idx값을 추가
def inorder(idx):
    if idx > n:
        return
    if (idx * 2) <= n:
        inorder(idx * 2)
    result.append(idx)
    if (idx * 2 + 1) <= n:
        inorder(idx * 2 + 1)

# 입력
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    result = [0]                    # 중위 표현 리스트 index값과 순서를 저장
    inorder(1)
    ans = [0, 0]                    # 결과에 필요한 값을 리스트에 담아서 언팩할 예정
    ans_1 = 1                       # 루트에 저장된 값 찾기 위한 변수
    ans_2 = n//2                    # n/2번 노드에 저장된 값 찾기 위한 변수
    for i in range(n+1):            # result 리스트 안에서 각각에 맞는 변수를 찾아서 변수에 맞는 idx값 찾기
        if result[i] == ans_2:
            ans[1] = i
        elif result[i] == ans_1:
            ans[0] = i

    print(f'#{tc}', end=' ')        # 출력
    print(*ans)

