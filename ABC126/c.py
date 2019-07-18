import math
N,K = list(map(int,input().split(" ")))


ans = 0

for p in range(1,N+1): # p 目
    if p >= K:
        ans += 1
    else:
        temp = K/p
        n = math.ceil(math.log2(temp))
        ans += (1/2)**n

ans /= N
print(ans)
