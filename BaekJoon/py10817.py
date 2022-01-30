# 세수 비교

A, B, C = map(int,input().split())
int_list = [A, B, C]

for i in range(len(int_list)):
    for j in range(len(int_list)-1):
        if int_list[j] > int_list[j+1]:
            int_list[j],int_list[j+1] = int_list[j+1],int_list[j]

print(int_list[len(int_list)//2])