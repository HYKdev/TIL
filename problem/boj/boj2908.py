# 상수

a, b = map(list, input().split())

flag = 0
for i in range(1, 4):
    if a[-i] > b[-i]:
        flag = 0
        break
    elif a[-i] < b[-i]:
        flag = 1
        break

if flag:
    result = b
else:
    result = a

for i in range(1, 4):
    print(result[-i], end='')
print()
