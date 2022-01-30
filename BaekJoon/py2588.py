A = int(input())
B = input()

B_100 = int(B[0])
B_10 = int(B[1])
B_1 = int(B[2])

result1 = A*(B_1)
result2 = A*(B_10)
result3 = A*(B_100)

print(result1)
print(result2)
print(result3)
print(result1+result2*10+result3*100)