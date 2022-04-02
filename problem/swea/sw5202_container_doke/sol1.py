import sys
sys.stdin = open('input.txt')

# 입력
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    time_list = []
    for _ in range(n):
        time_list.append(list(map(int, input().split())))

    # 도착 시간 기준으로 오름차순 정렬
    time_list.sort(key=lambda x: x[1], reverse=True)
    # 초기값
    ans = 1
    end = time_list.pop()[1]

    # 현재 저장된 도착시간과 다음 출발시간을 비교하여 같거나 크면 반복문 실행
    # 위에서 도착시간 기준으로 오름차순 정렬을 해뒀기 때문에
    # 현재 도착시간과 다음 출발시간만 비교하면 된다.
    """
    e1,  e2,  e3,   e4,   e5,  e6, .... en
    이라고 했을 때 도착지점 순서로 하나씩 꺼내서 스타트 지점이 이전 도착지점과
    현재 도착지점 사이에 있는게 최선의 결과여서 아래와 같이 반복문이 구성 됨
    """

    while time_list:
        s, e = time_list.pop()

        if end <= s:
            end = e
            ans += 1

    print(f'#{tc} {ans}')

