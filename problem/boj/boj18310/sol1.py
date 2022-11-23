# 18310 안테나

T = int(input())

antena_list = list(map(int, input().split()))

antena_list.sort()

middle_point1 = (antena_list[0] + antena_list[-1])//2
middle_point2 = (antena_list[0] + antena_list[-1])//2

total1 = 0
total2 = 0
result = 0
while True:
    if middle_point1 in antena_list or middle_point2 in minta_list:
        for item in antena_list:
            total1 += abs(item - middle_point1)
            total2 += abs(item - middle_point2)
        break
    
    middle_point2 += 1
    middle_point1 -= 1

if total1 != 0 and total2 != 0:
    if total1 > total2:
        result = middle_point2
    elif total1 < total2:
        result = middle_point1
    elif total1 == total2 :
        result = middle_point1

elif total1 == 0 and total2 != 0:
    result = middle_point2

elif total1 != 0 and total2 == 0:
    result = middle_point1

print(result)