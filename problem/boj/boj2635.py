# 수 이어가기
# 1,2를 포함해도 오류가 생기지 않기 (범위)
# 음수가 나오면 정지 or 전의 숫자보다 커지면 정지
# 최대 값 출력할 방법

# 입력
n = int(input())

# 출력의 최대 갯수 비교하기 위한 기준점
x = 1

# 두 번째 수 범위 설정 및 출력 리스트
for a in range(n//2,n+1):
    numbers = [n,a]
    i =1

# 이전 숫자보다 커지면 break
# 세 번째 이후 숫자 계산해서 리스트에 추가
    while True:
        if numbers[i-1] < numbers[i]:
            break
        else:
            numbers.append(numbers[i-1]-numbers[i])
            i+=1

# 출력 갯수 비교해서 최대 값 저장
    if x <= len(numbers):
        x = len(numbers)
        numbers_list = numbers

# 출력
print(x)
for j in range(len(numbers_list)):
    print(numbers_list[j], end=' ')