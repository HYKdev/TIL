V = int(input())
votes = input()

A_count = votes.count('A')
B_count = votes.count('B')

if A_count > B_count:
    print('A')
elif A_count < B_count:
    print('B')
else:
    print('Tie')