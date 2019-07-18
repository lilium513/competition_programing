import itertools
N,x = list(map(int,input().split(" ")))
As = list(map(int,input().split(" ")))
ans = 0
for i in range(0,N-1):
    l = As[i]
    r = As[i+1]
    diff = max((r+l) - x,0)
    if diff >= r:
        ans += r

        diff -= r
        As[i + 1] = r = 0
        ans += diff

    else:
        r -= diff
        As[i + 1] = r
        ans += diff

print(ans)




