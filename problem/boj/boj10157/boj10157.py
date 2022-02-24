c, r =map(int, input().split())
k=int(input())

# 넓이 초과면 0출력
if k>c*r:
    print(0)
# 이하면 시작
else:
# 초기 값 설정
    n = [r, c, r, c]
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    d = 0
    cnt = 0
    ti = 0
    tj = 1
# 움직일 때 마다 cnt 증가시켜서 k값 넘을 때까지 연산
    while(cnt < k):
        d= d % 4
        ti += di[d]*n[d]
        tj += dj[d]*n[d]
        cnt += n[d]
        if d % 2:
            n[0] -= 1
            n[2] -= 1
        else:
            n[1] -= 1
            n[3] -= 1
        d += 1
# 원하는 위치가 꼭지점이 아니라면 차이만큼 후진
    if k < cnt:
        d -= 1
        ti -= di[d]*(cnt-k)
        tj -= dj[d]*(cnt-k)
    print(tj, ti)
