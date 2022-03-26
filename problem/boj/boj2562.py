#최댓값
max_idx = 0
max_number = 0
for i in range(1, 10):
    number = int(input())
    if max_number < number:
        max_number = number
        max_idx = i

print(max_number)
print(max_idx)