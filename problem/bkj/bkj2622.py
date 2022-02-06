# 삼각형 만들기

N = int(input())

cnt =0
for i in range(1,N-1):
    for j in range(i,N-1):
        k = N-i-j
        if j > k:
            break
        if i+j > k:
            cnt +=1

print(cnt)


# 결과는 잘 나오나 python3 시간초과 / pypy3 제출가능
