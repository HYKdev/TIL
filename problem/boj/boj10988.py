words = input()

while len(words) > 1:
    if words[0] == words[-1]:
        words = words[1:-1]
    else:
        print('0')
        break
if len(words) < 2:
    print('1')