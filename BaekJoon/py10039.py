# 평균 점수

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

N_lists = [A,B,C,D,E]
sum = 0
for N_list in N_lists:
    if N_list < 40:
        N_list = 40
        sum += N_list
    else:
        sum += N_list

result = int(sum/len(N_lists))


print(result)