import sys
sys.stdin = open('input.txt')

# merge_sort를 위해서 함수 선언
# merge_sort 과정에서 분할은 이해되는데 합병이 아직 이해가 잘 안됨
# 다른 사람 코드 보고 이해중이나 왜 이렇게 진행되는지 버벅이는 중
def merge_arr(left_arr, right_arr):
    # 글로벌 선언해서 활용할 예정
    global answer
    #
    if left_arr[-1] > right_arr[-1]:
        answer += 1
    merge_list = []
    left_idx, right_idx = 0, 0
    n, m = len(left_arr), len(right_arr)

    while left_idx != n and right_idx != m:
        if left_arr[left_idx] <= right_arr[right_idx]:
            merge_list.append(left_arr[left_idx])
            left_idx += 1

        else:
            merge_list.append(right_arr[right_idx])
            right_idx += 1

    if left_idx != n:
        merge_list += left_arr[left_idx:]
    if right_idx != m:
        merge_list += right_arr[right_idx:]

    return merge_list

# 리스트에 원소가 1개가 될 때 까지 분할 하고 분할된 리스트를 merge_arr함수 담아서 호출
def divide_arr(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    left = divide_arr(a[:mid])
    right = divide_arr(a[mid:])
    return merge_arr(left, right)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # answer, arr에 원하는 출력을 얻기 위해서 선언
    answer = 0
    arr = divide_arr(arr)
    print(f'#{tc} {arr[N//2]} {answer}')