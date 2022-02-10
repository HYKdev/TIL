import sys

sys.stdin = open('input.txt')

T = 10
# 입력
# 리스트 받은 것을 transpose
for tc in range(1, T + 1):
    n = int(input())
    n_list = []
    for _ in range(n):
        n_list.append(list(map(int, input().split())))
    n_list = list(map(list,zip(*n_list)))

# cnt 초기화
# 리스트에 있는 0값을 제거한 후 1,2가 연속되는 값은 cnt 1씩 늘려서 결과제출
    cnt = 0
    for i in range(n):
        while 0 in n_list[i]:
            n_list[i].remove(0)
        for j in range(len(n_list[i])-1):
            if n_list[i][j] == 1 and n_list[i][j+1] == 2:
                cnt += 1

    print(f'#{tc} {cnt}')