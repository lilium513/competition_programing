
N,K =list(map(int,input().split(" ")))
As = list(map(int,input().split(" ")))
l = 0
import math
r = 0
ans = 0
total = 0
for r in range(N):
    total += As[r]
    while total>=K:

        total -=As[l]
        l += 1
    ans += l


print(ans)