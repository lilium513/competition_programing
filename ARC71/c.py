def fib(n):
    f = [0] * (n+1)
    f[0] = 1
    f[1] = 1
    f[2] = 2
    for i in range(3,n + 1):
        f[i] = f[i-1] + f[i-2]
    return f
N,M = list(map(int,input().split(" ")))
NUM = 1000000007
ans = 1
f = [-1] * (N+1)
f[0] = 1
f[1] = 1
for _ in range(M):
    now = int(input())
    f[now] = 0






for i in range(2,N+1):
    if f[i] == -1:
        f[i] = (f[i-1] + f[i-2])%NUM

ans = f[N]
print(ans )








