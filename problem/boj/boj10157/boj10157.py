
def seat_check(j, i , key):
    if j * i < key:
        return 0
    else:
        

c, r = map(int, input().split())
k = int(input())

if seat_check(c, r, k):
    print(*seat_check(c, r, k))
else:
    print(seat_check(c, r, k))
