import sys

sys.stdin = open('input.txt', 'rt', encoding='UTF8')


#테스트 케이스 입력
T = 10

for tc in range(1, T + 1):
    n = int(input())
    test = input()
    arr = list(input())
#결과 값 초기화
    rlt = 0

# arr탐색 범위가 인덱스 에러 생기지 않는 곳까지 탐색
    for i in range(len(arr)-len(test)+1):
#비교가 끝나면 사용할 변수 초기화
        cnt = 0
        j = 0
# 반복문을 통해서 찾을 문자열 길이만큼 탐색
        while j < len(test):
            if test[j] == arr[i]:
                cnt += 1
            else:
                break
            j += 1
            i += 1
# 문자열을 찾았으면 결과값에 추가
        if cnt == len(test):
            rlt += 1

# 출력
    print(f'#{tc} {rlt}')

