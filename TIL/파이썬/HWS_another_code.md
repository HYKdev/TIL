```python
n = int(input())

for i in range(1, (n//2)+1):
    if n% i == 0:
        print(i, end=' ')

print(n)
```

```python
lst = [1, 2, 3, 4]

lst.append(5)
print(lst)

lst.append([6,7])
print(lst)

lst.extend([8,9])
print(lst)

lst.extend("abcd")
print(lst)

# 1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, [6, 7]]
# [1, 2, 3, 4, 5, [6, 7], 8, 9]
# [1, 2, 3, 4, 5, [6, 7], 8, 9, 'a', 'b', 'c', 'd']
```

```python
for _ in range(len(numbers)):
	for i in range(len(numbers)-1):
		if numbers[i] > numbers[i+1]: 
    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
```

```python
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]

sorted_list = []
# num들을 오름차순 정렬
for i in range(len(numbers)):
    a = float('inf')
    for num in numbers:
        if a > num:
            a = num
    sorted_list.append(a) #최솟값을 구해 차례대로 sorted_list에 추가
    numbers.remove(a)

print(sorted_list)
print(sorted_list[len(sorted_list)//2])

# [11, 22, 23, 24, 24, 25, 31, 38, 49, 49, 51, 52, 60, 60, 61, 63, 64, 65, 66, 67, 68, 69, 71, 72, 
# 80, 80, 83, 85, 87, 90, 94, 96, 99]
# 64
```

```
```

