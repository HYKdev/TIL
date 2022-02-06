# OX퀴즈

T = int(input())

for _ in range(T):
    answers = input()
    grade = 0
    sum = 0
    for i in range(len(answers)):
        if answers[i] == 'O':
            grade += 1
            sum += grade
        elif answers[i-1] == answers[i] == 'O':
            grade += 1
            sum += grade
        elif answers[i] == 'X':
            grade = 0

    print(sum)