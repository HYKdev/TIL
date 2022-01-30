# 네 번째 점
a1, a2 = map(int,input().split())
b1, b2 = map(int,input().split())
c1, c2 = map(int,input().split())

x_lists = sorted([a1,b1,c1])
y_lists = sorted([a2,b2,c2])

for i in range(2):
    if x_lists[i] != x_lists[i+1] and i == 0:
        d1 = x_lists[i]   
    elif x_lists[i] != x_lists[i+1] and i == 1:
        d1 = x_lists[i+1]

for i in range(2):
    if y_lists[i] != y_lists[i+1] and i == 0:
        d2 = y_lists[i]   
    elif y_lists[i] != y_lists[i+1] and i == 1:
        d2 = y_lists[i+1]

print(d1, d2)