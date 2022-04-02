def powerset(idx, N):

    if idx == N:  # 종료 조건
# 함수 리턴전에 합이 10인 부분 집합 출력
        if sum(bit) == 10:
            for b in bit:
                if b > 0:
                    print(b, end=' ')
            print()
        return

# 부분집합 조합 만들기
    bit[idx] = a[idx]
    powerset(idx + 1, N)

    bit[idx] = 0
    powerset(idx + 1, N)

# 테스트 케이스 입력
a = [i for i in range(1, 11)]
N = len(a)
bit = [0] * N

powerset(0, N)