T = int(input())

for i in range(T):
    str_list = list(map(str,input().split()))
    
    for j in str_list:
        
        if j == '@':
            A = A * 3
        elif j == '%':
            A += 5
        elif j == '#':
            A -= 7
        else:
            A = float(j)

    print('%0.2f' %A)