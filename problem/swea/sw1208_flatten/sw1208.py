import sys

sys.stdin = open('input.txt')

# 테스트케이스 입력
T = 10

for tc in range(1, T + 1):
    n = int(input())
    dumpbox = list(map(int, input().split()))

# 덤프 반복구문
    while True:
# 덤프 횟수 채우면 break
        if n == 0:
            break

# 덤프 리스트의 최대값을 가지는 위치와 최소값을 가지는 위치 찾기
        dump_max = dumpbox[0]
        dump_min = dumpbox[0]
        max_idx = 0
        min_idx = 0

        for i in range(100):
            if dump_max <= dumpbox[i]:
                dump_max = dumpbox[i]
                max_idx = i
            if dump_min >= dumpbox[i]:
                dump_min = dumpbox[i]
                min_idx = i

# 횟수 차감 최대값에 있는 블록을 최소값이 있는 블록으로 이동
        n -= 1
        dumpbox[max_idx] -= 1
        dumpbox[min_idx] += 1

# 최대값과 최소값 찾기
        for i in range(100):
            if dump_max <= dumpbox[i]:
                dump_max = dumpbox[i]
                max_idx = i
            if dump_min >= dumpbox[i]:
                dump_min = dumpbox[i]
                min_idx = i

# 최대 높이와 최소 높이 차이 비교
        ans = dumpbox[max_idx] - dumpbox[min_idx]

        if ans == 1 or ans == 0:
            break

    print(f'#{tc} {ans}')

