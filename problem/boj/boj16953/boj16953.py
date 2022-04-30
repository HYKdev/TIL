# A -> B

# DFS 함수
# global 선언하여 최소의 연산 수를 갱신할 예정
# num이 b가 됬을 때 cnt값이 min_cnt보다 작을 때만 할당해서 최소 값만 찾기
# 2배 or 10배 + 1 을 for구문을 통한 DFS재귀 설정 
def DFS(num, cnt):
    global b, min_cnt
    if num == b and min_cnt > cnt:
        min_cnt = cnt
        return

    for i in [num * 2, num * 10 + 1]:
        if i <= b:
            DFS(i, cnt+1)

# 입력
# min 최솟값 기준이 명확하지 않아 무한대로 설정

a, b = map(int, input().split())
min_cnt = float('inf')

DFS(a, 0)

# DFS를 돌려도 min_cnt갱신이 없으면 -1 아니면 min_cnt + 1
result = 0
if min_cnt == float('inf'):
    result = -1
else:
    result = min_cnt + 1
print(result)