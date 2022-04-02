import sys
sys.stdin = open('input.txt')

# 베이진 체크 함수
def run_triplet(lst):
    count_list = [0 for _ in range(10)]
    for number in lst:
        count_list[number] += 1

    for i in range(10):
        if count_list[i] >= 3:
            return True

    for i in range(8):
        if count_list[i] and count_list[i+1] and count_list[i+2]:
            return True

    return False

# 입력
T = int(input())
for tc in range(1, T + 1):
    card_list = list(map(int, input().split()))
    # stack_1을 플레이1 stack_2를 플레이2 로 잡고
    # 6장부터 베이비 진이 나오기 때문에 4장 먼저 나눠준 후 반복문 시작
    stack_1 = [card_list[0], card_list[2]]
    stack_2 = [card_list[1], card_list[3]]
    card_list = card_list[4:]
    ans = 0

    # 카드 한장씩 나눠 준 후 두 플레이어중 베이비진이 나오면
    # ans 값 바꾸고 반복문 종료 조건문에 아무것도 안걸리면 ans 초기 값 반환
    while card_list:
        stack_1.append(card_list[0])
        stack_2.append(card_list[1])
        card_list = card_list[2:]

        if run_triplet(stack_1):
            ans = 1
            break
        elif run_triplet(stack_2):
            ans = 2
            break

    print(f'#{tc} {ans}')

