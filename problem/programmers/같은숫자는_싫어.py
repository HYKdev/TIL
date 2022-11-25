from collections import deque

def solution(arr):
    answer = deque()
    
    if len(arr) > 0:
        answer.appendleft(arr.pop())
    
    while True:
        if len(arr) == 0:
            break
        
        item = arr.pop()
        if answer[0] != item:
            answer.appendleft(item)
    
    return answer


arr = [1,1,3,3,0,1,1]
print(solution(arr))