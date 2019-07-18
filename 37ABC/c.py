N,K =list(map(int,input().split(" ")))
As = list(map(int,input().split(" ")))
before = sum(As[:K])
ans = before
for i in range(K,N):
    ans += before-As[i-K]+As[i]
    before = before-As[i-K]+As[i]
print(ans)