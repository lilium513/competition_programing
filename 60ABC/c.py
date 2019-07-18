import itertools
import math
N , T=  list(map(int,input().split(" ")))
times = list(map(int,input().split(" ")))
ans = 0
for i in range(N-1):
    ans += min (T,times[i+1]-times[i])

ans += T
print(ans)