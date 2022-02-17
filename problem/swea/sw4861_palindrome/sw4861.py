import sys
from pprint import pprint
sys.stdin = open('input.txt')

#테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    data1 = []
    for _ in range(n):
        data1.append(list(input()))
# transpose
    data2 = list(map(list, zip(*data1)))
# 연산에 사용할 변수 초기화
    result = []
    i = 0
# m이 짝수일 때와 홀수일 때 각각 조건 생성
# m 길이만큼 회문인지 테스트해서 회문이면 결과에 저장
    if m%2 == 0:
        for i in range(n-m+1):
            for data in data1:
                if data[i:i+m//2] == data[i+m-1:i+m//2-1:-1]:
                    result = data[i:i+m]
            for data in data2:
                if data[i:i+m//2] == data[i+m-1:i+m//2-1:-1]:
                    result = data[i:i+m]
    else:
        for i in range(n-m+1):
            for data in data1:
                if data[i:i+m//2] == data[i+m-1:i+m//2:-1]:
                    result = data[i:i+m]
            for data in data2:
                if data[i:i+m//2] == data[i+m-1:i+m//2:-1]:
                    result = data[i:i+m]

# 결과에 맞는 출력을 위해 리스트를 문자열로 변환
    rlt = ''
    for ch in result:
        rlt += ch

    print(f'#{tc} {rlt}')

