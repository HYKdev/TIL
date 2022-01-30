A , B = map(int,input().split())
C = int(input())

B = B + C

while B >= 60:
        A = A+1
        B = B-60

while A>=24:
    A = A-24

print(A, B)