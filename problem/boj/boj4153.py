# 직각 사각형

while True:
    x, y, z = map(int, input().split())
    arr = [x,y,z]
    arr.sort()
    if x == y == z == 0:
        break

    if arr[2]**2 == arr[1]**2 + arr[0]**2:
        print('right')
    else:
        print('wrong')