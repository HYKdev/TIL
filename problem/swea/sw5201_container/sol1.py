import sys
sys.stdin = open('input.txt')

# 화물과 트럭 중량을 비교해서 담을 수 있으면 트럭을 0처리하고 반환
# 맞는 조건이 없다면 0을 반환 (0 반환 안하면 None이 나와서 연산이 안됨)
def check(weight):
    for j in range(1, len(load_capacity)+1):
        if weight <= load_capacity[-j]:
            load_capacity[-j] = 0
            return weight
    return 0

# 입력
T = int(input())
for tc in range(1, T + 1):
    container, truck = map(int, input().split())
    freight = list(map(int, input().split()))
    load_capacity = list(map(int, input().split()))

    # 정렬해서 -index를 활용할 예정
    freight.sort()
    load_capacity.sort()

    # 화물의 무게
    total = 0
    # 화물의 개수 만큼 반복문으로 비교해서 총 중량에 담을 예정
    for i in range(1, len(freight)+1):
        total += check(freight[-i])

    print(f'#{tc} {total}')

