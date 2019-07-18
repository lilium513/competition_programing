import math
N,M = list(map(int,input().split(" ")))
ll = -10e9
rr = (10e9)
for i in range(M):
    l,r = list(map(int, input().split(" ")))
    if l > ll:
        ll = l
    if r  <  rr :
        rr = r
ans = max(rr - ll + 1,0)
print(ans)