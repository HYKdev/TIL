# 설탕 배달

N = int(input())

N_list = []
for i in range((N//5)+1):
    for j in range((N//3)+1):
        if 5*i+3*j == N:
            N_list.append(i+j)

if len(N_list) == 0:
    print(-1)
else:
    print(min(N_list))
