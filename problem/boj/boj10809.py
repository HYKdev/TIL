# 알파벳 찾기

S = list(input())

arr = [-1 for _ in range(26)]

#97~122 a~z
i = 0
for s in S:
    num = ord(s)-97
    if arr[num] == -1:
        arr[num] = i
    i += 1

print(*arr)