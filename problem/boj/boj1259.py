# 팰린드롬수

while True:
    test = list(map(int, input()))

    if test[0] == 0:
        break
    result = 'yes'
    for i in range(len(test)//2):
        if test[i] != test[-1-i]:
            result = 'no'
            break
    print(result)