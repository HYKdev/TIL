
def number_sort(args):
    for i in range(n):
        for j in range(n-1):
            if args[j] > args[j+1]:
                args[j], args[j+1] = args[j+1], args[j]
    return args


n = int(input())
n_list = []

for _ in range(n):
    n_list.append(int(input()))

number_sort(n_list)

ans = [0, 0, 0, 0]

ans[0] = round(sum(n_list)/n)
ans[1] = n_list[n//2]
ans[2] = 0
ans[3] = n_list[0]-n_list[-1]

counts = dict()
for i in range(1,n+1) :
	counts[i] = []


