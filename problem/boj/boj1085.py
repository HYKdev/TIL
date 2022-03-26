# 직사각형

x, y, w, h = map(int, input().split())

ans = min(x, y, abs(x-w),abs(y-h))

print(ans)