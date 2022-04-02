import sys
sys.stdin = open('input.txt')

# 예를 들어 10을 찾는 경우 오른쪽-오른쪽 구간을 선택하므로 조건에 맞지 않는다
# 서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다.

# 이진 탐색 함수
def binary_search(lst1, find_value):
    # 글로벌 선언해서 체크할 예정
    global cnt
    # 시작 끝 idx잡고 history로 방향 설정
    start = 0
    end = n - 1
    history = 0
    # 종료 조건은 시작점이 끝점보다 크거나 mid위치에 찾는 값이 있으면 종료
    # 찾는 값이 mid위치보다 왼쪽에 있는데 1이거나 찾는 값이 mid위치보다 오른쪽에 있으면 탐색 종료

    while start <= end:
        mid = (start + end) // 2
        if lst1[mid] == find_value:
           cnt += 1
           return

        elif lst1[mid] < find_value:
            if history == 2:
                break
            else:
                start = mid + 1
                history = 2

        elif lst1[mid] > find_value:
            if history == 1:
                break
            else:
                end = mid - 1
                history = 1

# 입력
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    # a_list 정렬
    a_list.sort()
    # 갯수 측정할 변수 초기화
    cnt = 0
    # b_list에 하나씩 꺼내서 이진탐색 진행
    for b_args in b_list:
        binary_search(a_list, b_args)

    print(f'#{tc} {cnt}')

