# 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

result = A * B * C
count_lst = [0 for _ in range(10)]

while True:
    count_lst[result % 10] += 1

    if result // 10:
        result = result//10
    else:
        break
    
for i in count_lst:
    print(i)