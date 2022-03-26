import sys
sys.stdin = open('input.txt')

from itertools import combinations

# 입력
T = int(input())
for tc in range(1, T + 1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    # 최대 길이 체크 (min_ans 기준점 잡기 위해서 한거지만 사실 필요 없음)
    s = sum(arr)
    min_ans = s
    # combination 모든 경우의 수를 체크하기 위해서 1~최대 갯수까지 반복함
    # 합이 b보다는 크거나 같아야하고 b와의 차이가 min_ans보다 작으면 min_ans 체인지
    for i in range(len(arr), 0, -1):
        for combi_list in combinations(arr, i):
            combi_list_sum = sum(combi_list)
            if combi_list_sum >= b and combi_list_sum - b < min_ans:
                min_ans = combi_list_sum - b

    print(f'#{tc} {min_ans}')

