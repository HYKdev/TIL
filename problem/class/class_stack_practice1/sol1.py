

arr = []

for i in range(1, 4):
    arr.append(i)

for _ in range(len(arr)):
    print(arr.pop())
# ---------------------------------------------------------------------

def stack_test(lst):
    count_arr = []
    for i in range(len(lst)):
        if lst[i] == '(':
            count_arr.append('(')
        elif len(count_arr) == 0 and lst[i] == ')':
            return False
        elif lst[i] == ')' and len(count_arr) > 0:
            count_arr.pop()
    if len(count_arr) == 0:
        return True
    else:
        return False

arr1 = '()()((()))'
arr2 = '((()((((()()((()())((())))))'

print(stack_test(arr1))
print(stack_test(arr2))
