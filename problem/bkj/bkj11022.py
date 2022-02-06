T = int(input())

for i in range(T):
    A, B = map(int,input().split())
    R = A + B
    print(f'Case #{i+1}: {A} + {B} = {R}')