# 사분면

n = int(input())
cnt, cnt_1, cnt_2, cnt_3, cnt_4 = 0, 0, 0, 0, 0
for i in range(n):
    xi, yi =map(int,input().split())

    if xi>0 and yi>0:
        cnt_1 += 1
    elif xi<0 and yi>0:
        cnt_2 += 1
    elif xi<0 and yi<0:
        cnt_3 += 1
    elif xi>0 and yi<0:
        cnt_4 += 1
    else:
        cnt += 1

print(f'Q1: {cnt_1}')
print(f'Q2: {cnt_2}')
print(f'Q3: {cnt_3}')
print(f'Q4: {cnt_4}')
print(f'AXIS: {cnt}')