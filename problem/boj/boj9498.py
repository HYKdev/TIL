# 시험성적

T = int(input())

if 100>= T >= 90:
    result = 'A'
elif 89 >= T >= 80:
    result = 'B'
elif 79 >= T >= 70:
    result = 'C'
elif 69 >= T >= 60:
    result = 'D'
else:
    result = 'F'

print(result)