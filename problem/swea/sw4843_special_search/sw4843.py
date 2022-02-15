import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    special_list = list(map(int, input().split()))

# sort 정렬
    for i in range(n):
        for j in range(n-1):
            if special_list[j] < special_list[j+1]:
                special_list[j], special_list[j+1] = special_list[j+1], special_list[j]

# 결과 값 리스트 초기화
# 인덱스의 양쪽 끝값을 찾아서 리스트에 추가
    result = []
    for i in range(5):
        result.extend([special_list[i], special_list[-1-i]])

# 출력
    print(f'#{tc}', end=' ')
    for i in range(10):
        print(result[i], end=' ')
    print()
