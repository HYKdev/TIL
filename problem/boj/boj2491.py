# 수열

# 입력 값
N = int(input())
N_list = list(map(int,input().split()))

# 최소 길이 값을 1 비교군 1로 두고 시작
cnt = 1
N_max = 1

# 증가하는 값의 최대길이
for i in range(1,N):
    if N_list[i-1] <= N_list[i]:
        cnt += 1
    else:
        cnt = 1
    if N_max < cnt:
        N_max = cnt

# 감소하는 값의 최대 길이
cnt = 1
for i in range(1,N):
    if N_list[i-1] >= N_list[i]:
        cnt += 1
    else:
        cnt = 1
    if N_max < cnt:
        N_max = cnt

# 출력
print(N_max)