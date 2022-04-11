# 듣보잡

n, m = map(int, input().split())

n_list = []

for _ in range(n):
    n_list.append(input())

m_list = []

for _ in range(m):
    m_list.append(input())

cnt = 0
ans = []
for item in n_list:
    if item in m_list:
        cnt += 1
        ans.append(item)
ans.sort()
print(cnt)
for item in ans:
    print(item)