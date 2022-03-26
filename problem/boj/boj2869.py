# 달팽이는 올라

a, b, v =map(int, input().split())
result = 0
i = 1
while True:
    if (v-a)//(a-b)*(a-b) + i * a >= v:
        result = (v-a)//(a-b) + i
        break
    i += 1

print(result)