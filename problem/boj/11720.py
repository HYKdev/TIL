# 숫자의 합

n = int(input())
number = list(map(int, input()))

total = 0
for num in number:
    total += num

print(total)