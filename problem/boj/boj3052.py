# 나머지

cnt_list = set()
for _ in range(10):
    number = int(input())
    cnt_list.add(number%42)

print(len(cnt_list))