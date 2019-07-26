N = input()
N = int(N)
Ws = list(map(int,input().split(" ")))

ans = 10e10
for i in range(1,N):
    if abs(sum(Ws[:i])-sum(Ws[i:])) < ans:
        ans = abs(sum(Ws[:i])-sum(Ws[i:]))
print(ans)
