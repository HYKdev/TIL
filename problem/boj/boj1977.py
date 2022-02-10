# 완전제곱수
import math as ma

M = int(input())
N = int(input())
ma_list = []
for i in range(ma.ceil(M**0.5),ma.ceil(N**0.5)+1):
    if M <= i**2 <= N:
        ma_list.append(i**2)

if len(ma_list) == 0:
    print(-1)
else:
    print(sum(ma_list))
    print(ma_list[0])