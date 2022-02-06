# 더하기 사이클

N = input()

if 0 <= int(N) < 10:
    N = '0'+ N

cnt = 1
i = 1
N = N + str((int(N[i-1])+int(N[i]))%10)
i += 1 

while True:
    if N[0]+N[1] == N[i-1]+N[i] or N == '0':
        break
    else:
        N = N + str((int(N[i-1])+int(N[i]))%10)
        i += 1
        cnt += 1
print(cnt)