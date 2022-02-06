# 첼시를 도와줘

n = int(input())


for _ in range(n):
    c_list = []
    name_list = []
    p = int(input())
    for _ in range(p):
        c, name = input().split()
        c = int(c)

        c_list.append(c)
        name_list.append(name)
    
    for i in range(p):
        if c_list[i] == max(c_list):
            print(name_list[i])
