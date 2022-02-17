import sys

sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    cnt = 0

# 첫 번째 문자열의 첫글자가 두번째 문자열에 같은게 있고
# 같은 글자 기준 첫 번째 문자열의 길이만큼 슬라이싱 했을 때 같으면
# cnt 1추가
    for i in range(len(str2)):
        if str1[0] == str2[i] and str1 == str2[i:i+len(str1)]:
            cnt += 1


    print(f'#{tc} {cnt}')

