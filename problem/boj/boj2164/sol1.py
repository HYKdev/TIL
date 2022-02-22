# n장의 카드
# 1~n까지 번호가 있고 (앞)1~n순서로 놓여있다.
# 가장 가까운 2**n에서 차이만큼 2빼기
n = int(input())

for i in range(n//2+2):
    if n - 2**i <= 0:
        print(2**i-2*(abs(n-2**i)))
        break