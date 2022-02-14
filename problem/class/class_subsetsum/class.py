import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    sub_list = list(map(int, input().split()))
# 음수 양수 분류 및 결과값 초기화
    sub_pos = []
    sub_neg = []
    rlt = 0

    cnt1 = 0
    cnt2 = 0
    for i in range(len(sub_list)):
        if sub_list[i] > 0:
            cnt1 += 1
            sub_pos.append(sub_list[i])
        if sub_list[i] < 0:
            cnt2 += 1
            sub_neg.append(sub_list[i])

# 다 음수이거나 양수이면 결과는 0
    if cnt1 == len(sub_list) or cnt2 == len(sub_list):
        rlt = 0


    else:
# 부분집합 합 리스트에 필요한 길이 및 리스트 선언
        len_neg = len(sub_neg)
        len_pos = len(sub_pos)
        sum_neg_list = []
        sum_pos_list = []
# 음수의 부분집합 합 리스트
        for i in range(1<<len_neg):
            sum_neg = 0
            for j in range(len_neg):
                if i & (1<<j):
                    sum_neg += sub_neg[j]
            sum_neg_list.append(sum_neg)

# 양수의 부분집합 합 리스트
        for i in range(1<<len_pos):
            sum_pos = 0
            for j in range(len_pos):
                if i & (1<<j):
                    sum_pos += sub_pos[j]
            sum_pos_list.append(sum_pos)

# 공집합은 제외하기 위해 슬라이싱
        sum_neg_list = sum_neg_list[1:]
        sum_pos_list = sum_pos_list[1:]

# 부분집합 합 리스트를 비교하여 합이 0되는 것 찾기
        for n in sum_neg_list:
            for m in sum_pos_list:
                if n + m == 0:
                    rlt = 1
# 결과
    print(f'#{tc} {rlt}')

