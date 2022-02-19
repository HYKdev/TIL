# 맥주 냉장고

n = int(input())

i = 2
arr = []
while n > 1:
    if n % i == 0:
        arr.append(i)
        n = n//i
    else:
        i += 1

print(arr)