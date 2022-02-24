def powerset(idx, N):

    if idx == N:  # 종료 조건
# 함수 리턴전에 합이 10인 부분 집합 출력
        if sum(bit) == 10:
            print(bit)
        return

# 부분집합 조합 만들기
    bit[idx] = a[idx]
    powerset(idx + 1, N)

    bit[idx] = 0
    powerset(idx + 1, N)

# 테스트 케이스 입력
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(a)
bit = [0] * N

powerset(idx=0, N=N)