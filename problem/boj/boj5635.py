# 생일

n = int(input())

name_list = []
day_list = []

for _ in range(n):
    name, dd, mm, yyyy = input().split()

    if len(dd) == 1:
        dd = '0'+dd
    
    if len(mm) == 1:
        mm = '0'+mm
    
    name_list.append(name)
    day_list.append(yyyy+mm+dd)

for i in range(n):
    if day_list[i] == max(day_list):
        print(name_list[i])

for i in range(n):
    if day_list[i] == min(day_list):
        print(name_list[i])





