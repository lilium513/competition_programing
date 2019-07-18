

import math
N,K = list(map(int,input().split(" ")))
nums = (K) * [0]
for i in range(1,N+1):
    nums[i%K] += 1
ans = 0
for a in range(K):
    b = (K-a) % K 
    c = (K-a) % K
    if (2 * K - 2 * a) % K != 0:
        continue
    # print("a,b,c = ",a,b,c)
    # print("nums:",nums)
    ans += nums[a] * nums[b] * nums[c]

print(ans)