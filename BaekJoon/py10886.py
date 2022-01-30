# 0 = not cute / 1 = cute

N = int(input())
vote_list = []
for i in range(N):
    vote_list.append(input())

vote_cute = vote_list.count('1')
vote_notcute = vote_list.count('0')

if vote_cute > vote_notcute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')