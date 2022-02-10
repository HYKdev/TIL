# 소수 찾기

N = int(input())

numbers = list(map(int,input().split()))
sosu = 0
for number in numbers:
    cnt = 0
    for i in range(1, number+1):
        if number%i == 0:
            cnt +=1
    if cnt == 2:
        sosu += 1
print(sosu)
