# 문자열 반복

T = int(input())

for i in range(T):
    R, S = map(str,input().split())
    R = int(R)
    result = ''
    for j in S:
        result += R * j

    print(result)