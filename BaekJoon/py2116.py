# 주사위 쌓기

# 주사위 아래(윗면) = 주사위 위(아래면)

# 숫자의 합 최댓값

# A-F / B-D / C-E
# 0-5 / 1-3 / 2-4 인덱스로 연결
# 아래 위면을 제외한 가장 큰 값 sum
# 결과값 저장해서 비교 후 가장 큰 값을 출력
# 1층기준 6가지 경우의 수가 있음

n = int(input())
dice= []
for i in range(n):
    dice_list = list(map(int,input().split()))

    dice.append(dice_list)



#[[2, 3, 1, 6, 5, 4], 
# [3, 1, 2, 4, 6, 5], 
# [5, 6, 4, 1, 3, 2], 
# [1, 3, 6, 2, 4, 5], 
# [4, 1, 6, 5, 2, 3]]