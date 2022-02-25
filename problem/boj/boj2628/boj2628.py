# 종이 자르기


j, i = map(int, input().split())

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
lst_i = [0,i]
lst_j = [0,j]

for lst in arr:
    if lst[0] == 1:
        lst_j.append(lst[1])
    elif lst[0] == 0:
        lst_i.append(lst[1])

lst_i.sort(reverse=True)
lst_j.sort(reverse=True)
max_size = lst_i[-1]*lst_j[-1]
for lst_ii in range(len(lst_i)-1):
    for lst_jj in range(len(lst_j)-1):
            size = (lst_i[lst_ii]-lst_i[lst_ii+1]) * (lst_j[lst_jj]-lst_j[lst_jj+1])
            max_size = max(max_size, size)

print(max_size)