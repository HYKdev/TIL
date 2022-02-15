import sys

sys.stdin = open('input.txt')

T = int(input())

# 테스트 케이스 입력
for tc in range(1, T + 1):
    n, k = map(int, input().split())

# 1~12까지 집합 리스트 생성 및 길이 선언
    subset_list = []
    for i in range(1, 13):
        subset_list.append(i)
    sub = len(subset_list)

# 1~12까지의 부분집합을 만들기
    subset__sum_list = []
    for i in range(2**sub):
        sub_list = []
        for j in range(sub):
            if i & (1<<j):
                sub_list.append(subset_list[j])
        subset__sum_list.append(sub_list)

# 1~12까지의 부분 집합 중 길이가 n인 경우 합산
# 합산 결과가 k와 같으면 cnt 1증가
    cnt = 0
    for sum_list in subset__sum_list:
        sum = 0
        if len(sum_list) == n:
            for i in range(len(sum_list)):
                sum += sum_list[i]
        if sum == k:
            cnt += 1


    print(f'#{tc} {cnt}')

