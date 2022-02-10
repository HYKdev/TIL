# 그릇

dish = input()
sum = 10
for i in range(len(dish)-1):
    if dish[i] == dish[i+1]:
        sum += 5
    else:
        sum += 10

print(sum)
