# 나이순 정렬

n = int(input())
arr = [[] for _ in range(201)]
for _ in range(n):
    age, name = input().split()
    arr[int(age)].append(name)


for i in range(len(arr)):
    if arr[i]:
        for item in arr[i]:
            print(i, end=" ")
            print(item)