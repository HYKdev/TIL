
# 최대공약수 와 최소공배수
# 유클리드 호제법!
def num_div(n, m):
    while True:
        if m == 0:
            break
        n, m = m, n%m
    return n

n, m = map(int, input().split())


print(num_div(n, m))
print(int(n*m/num_div(n, m)))