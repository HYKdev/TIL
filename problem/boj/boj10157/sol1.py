# 자리배정
# 
def check(j, i, key):
    i_sum = 0
    j_sum = 0
    if  j * i < key:
        return 0
    else:
        j -= 1
        for a in range(key):
            if (a+1)*(j+i-a) > key:
                break
        for b in range(i, i-1-a, -1):
            i_sum += b*((-1)**(i-b))
        for c in range(j, j-1-a, -1):
            j_sum += c*((-1)**(j-c))
        if a % 2 == 0:
            if (a+1)*(j+i-a)-key > j-a:
                j_sum -= j-a-1
                i_sum -= (a+1)*(j+i-a)-key-j+a
            elif (a+1)*(j+i-a)-key <= j-a:
                j_sum -= j-a-1
        else:
            if (a+1)*(j+i-a)-key > j-a:
                j_sum += j-a-1
                i_sum += (a+1)*(j+i-a)-key-j+a
            elif (a+1)*(j+i-a)-key <= j-a:
                j_sum += j-a-1
        return [j_sum, i_sum]

c, r = map(int, input().split())
k = int(input())

if check(c, r, k):
    print(*check(c, r, k))
else:
    print(check(c, r, k))