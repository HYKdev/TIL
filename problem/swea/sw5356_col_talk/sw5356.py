import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    arr = []
    for _ in range(5):
        arr.append(list(input()))
# 결과 초기화 및 가장 긴 리스트 찾기
    rlt = ''
    max_len = 0
    for element in arr:
        if max_len < len(element):
            max_len = len(element)

# 가장 긴 리스트보다 짧은 리스트는 차이 만큼 ''문자열 추가
    for element in arr:
        if len(element) < max_len:
            element += ['']*(max_len-len(element))

# transpose
    data = list(map(list, zip(*arr)))

# transpose한 리스트를 하나씩 꺼내서 결과값에 추가
    for element in data:
        for i in range(len(element)):
            rlt += element[i]

# 출력
    print(f'#{tc} {rlt}')
