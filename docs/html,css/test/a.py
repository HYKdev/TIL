import random as rd

class ClassHelper():
    def __init__(self, list):
        self.stud_list = list

    def pick(self, n):
        return_list = []
        while True:
            if len(return_list) == n:
                break
            num = rd.randint(0, len(self.stud_list) - 1)
            if self.stud_list[num] not in return_list:
                return_list.append(self.stud_list[num])
            else:
                continue
        return(return_list)

    def match_pair(self):
        import random
        result = []
        random.shuffle(self.students)

        for i in range(len(self.students)//2):
            if len(self.students) <= 3:
                result = result + [self.students]
            else:
                a = self.students.pop()
                b = self.students.pop()
                pair = [a] + [b]
                result.append(pair)
        return result

ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])

print(ch.pick(1)) #=> ['이싸피']
print(ch.pick(1)) #=> ['김싸피']
print(ch.pick(2)) #=> ['김싸피', '박싸피']
print(ch.pick(3)) #=> ['김싸피', '조싸피', '정싸피']
print(ch.pick(4)) #=> ['박싸피', '이싸피', '김싸피', '정싸피']

print(ch.match_pair()) #=> [['조싸피', '이싸피'], ['김싸피', '정싸피', '박싸피']]