# 연산자 끼워넣기

def DFS(cnt, value, plus, minus, multi, div):
    global max_value, min_value
    if cnt == n:
        max_value = max(value, max_value)
        min_value = min(value, min_value)
    
    
    if plus:
        DFS(cnt+1, value + arr[cnt], plus-1, minus, multi, div)
    if minus:
        DFS(cnt+1, value - arr[cnt], plus, minus-1, multi, div)
    if multi:
        DFS(cnt+1, value * arr[cnt], plus, minus, multi-1, div)
    if div:
        DFS(cnt+1, int(value / arr[cnt]), plus, minus, multi, div-1)

n = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))
max_value = -float('inf')
min_value = float('inf')


DFS(1, arr[0], oper[0], oper[1], oper[2], oper[3])

print(max_value)
print(min_value)