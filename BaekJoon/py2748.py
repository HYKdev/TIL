# 피보나치 수2

n = int(input())

fibo = [0,1]
i = 0
while n != i:
    fibo.append(fibo[i]+fibo[i+1])
    i += 1

print(fibo[i])