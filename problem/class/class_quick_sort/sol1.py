import sys
sys.stdin = open('input.txt')

# 퀵 소트 함수
def quick_sort(array, start, end):
    # 퀵 소트 종료 조건
    # 오른쪽 탐색이 왼쪽보다 작아지면 종료
    if start >= end:
        return
    # 피봇 지점을 시작점부터 시작해서 탐색 시작
    pivot = start
    left = start + 1
    right = end
    # 왼쪽 탐색이 오른쪽 보다 커지면 종료
    # 왼쪽 탐색이 end 보다 작거나 같고 피봇 기준 값이 작거나 같으면 left 증가
    # 오른쪽 탐색이 시작보다 작고 피봇 기준 값보다 크거나 같으면 right 증가
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        # 반복문을 통해서 left, right 가 정해지면 자리 교체
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    # 재귀 호출해서 정렬될 때 까지 반복
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

# 입력
T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    # 퀵 소트 호출
    quick_sort(numbers, 0, len(numbers) - 1)

    print(f'#{tc} {numbers}')

