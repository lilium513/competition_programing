import math
N,W = list(map(int, input().split(" ")))

items= [list(map(int, input().split(" "))) for _ in range(N)]


dp = [[0 for _ in range(W+1)] for _ in range(N + 1) ]
for w_sum in range(W + 1):
    for i in range(N):


        w,v = items[i]
        if w_sum - w >= 0:
            dp[i + 1][w_sum]  = dp[i][w_sum - w] + v
        # print(dp[i + 1][w],dp[i][w])
        a,b = dp[i + 1][w_sum],dp[i][w_sum]
        dp[i + 1][w_sum] = max(a,b)

print(dp[-1][-1])


