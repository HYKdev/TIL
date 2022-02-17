import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()

# 길이 선언 및 변수 초기화
    n = len(A)
    m = len(B)
    i = 0
    cnt = 0
# B문자열의 첫번째 단어가 A에 있다면 슬라이싱해서 비교하여
# 같으면 길이만큼 건너 뛰고 아니면 그 다음 인덱스와 비교
    while i < n:
        if A[i] == B[0]:
            if A[i:i+m] == B:
                i += m
                cnt += 1
            else:
                i += 1
                cnt += 1
        else:
            i += 1
            cnt += 1

# 출력
    print(f'#{tc} {cnt}')

