N  = int(input())
As = list(map(int,input().split(" ")))
appeared = [False] * (10**5 + 5 )
l = 0
r = 0
ans = 0
total = 0
for l in range(N):
    while r < N and not appeared[As[r]] :
        appeared[As[r]] = True
        ans = max(r - l + 1, ans)
        r += 1

    appeared[As[l]] = False


print(ans)