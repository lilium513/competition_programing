N = int(input())
hasiras  =  list(map(int,input().split(" ")))
dp = [10000 * 100001 ] * N
dp[0] = 0
for i,hasira in enumerate(hasiras[:-1]):
    dp[i+1] = min(dp[i+1],dp[i] +abs (hasiras[i] - hasiras[i+1]))
    if i + 2 < N:
        dp[i+2] = min(dp[i+2],dp[i] + abs(hasiras[i] - hasiras[i+2]))


print(dp[N-1])
