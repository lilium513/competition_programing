import math
N = int(input())
dp = [10**15] * 1000000
dp[1] = 1
dp[0] = 0
for i in range(N + 1):
    dp[i + 1] = min (dp[i] + 1 , dp[i + 1])
    for k in range(7):
        dp[i + 6 ** k ] = min (dp[i] + 1 ,dp[i + 6 ** k ])
    for k in range( 7):
        dp[i + 9 ** k] = min(dp[i] + 1, dp[i + 9 ** k])
print(dp[N])