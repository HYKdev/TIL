# 스위치 켜고 끄기
# 남학생은 자기 번호의 배수의 자리를 바꾼다.
# 여학생은 자기 번호 중심으로 좌우가 대칭인 구간 까지 교체
# 대칭이 없다면 본인 자리만 교체

n = int(input())

switchs = list(map(int,input().split()))

students = int(input())

for _ in range(students):
    gender, position = map(int,input().split())

    if gender == 1:
        i = 1
        while position*i <= n:
            switchs[position*i-1] = abs(1-switchs[position*i-1])
            i +=1
    
    elif gender == 2:
        cnt = 0
        S = position - 1
        E = position - 1
        while True:
            if S-cnt < 0 or E+cnt >= n or switchs[S-cnt] != switchs[E+cnt]:
                cnt -= 1
                break
            cnt += 1
        
        for j in range(S-cnt,E+cnt+1):
            switchs[j] = abs(1-switchs[j])

for k in range(0, n, 20):
    print(' '.join(map(str,switchs[k:k+20])))