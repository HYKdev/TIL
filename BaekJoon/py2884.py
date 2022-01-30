# 알람 시계

H, M = map(int,input().split())

if M-45 < 0:
    H -= 1
    M += 15
else:
    M -= 45

if H < 0:
    H += 24
else:
    H = H

print(H, M)