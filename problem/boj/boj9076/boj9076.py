# 점수집계

# 


T = int(input())

for _ in range(T):
    scores = list(map(int, input().split()))

# sort 정렬
    scores.sort()
# 최대 최소 제외
    scores = scores[1:-1]
# 최대 최소 차이 4점이상일 경우 KIN 아니면 sum 출력
    if scores[-1] - scores[0] >=4:
        print('KIN')
    else:
        print(sum(scores))
