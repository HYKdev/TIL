import sys
sys.stdin = open('input.txt')

# 함수 선언
def insert_heap(data):
    heap.append(data)                                       # edges 값들을 힙에 넣어주기
    idx = len(heap)-1                                       # 탐색할 범위의 인덱스 에러 방지를 위해서 -1
    while idx > 1 and heap[idx] < heap[idx//2]:             # 단축평가 및 반복문 오류를 방지하기 위해서
        heap[idx], heap[idx//2] = heap[idx//2], heap[idx]   # idx > 1 앞에 추가하였음
        idx = idx // 2                                      # 조건을 만족할 때까지 자식노드와 부모 노드 값을 교체

# 입력
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    edges = list(map(int, input().split()))
# 힙이라는 리스트를 선언하여 edge 값들을 문제의 조건에 맞게 담을 예정
    heap = [0]

# 엣지 리스트에 있는 값들을 맨 앞에서부터 받아와서 함수로 처리할 예정
    for edge in edges:
        insert_heap(edge)
# 조상노드의 합을 찾아야해서 ans를 선언하고 n//2로 반복해서 합산
    ans = 0
    while n:
        n = n // 2
        ans += heap[n]

    print(f'#{tc} {ans}')

