N = int(input())
hs = list(map(int,input().split(" ")))
INF = 10 ** 15
dp = [INF] * N
dp[0] = 0
dp[1] = abs(hs[0] - hs[1])
for i in range(2,N):
    dp[i] = min(dp[i-1]+  abs(hs[i-1] - hs[i]) , dp[i] ,dp[i-2]+  abs(hs[i-2] - hs[i]))
print(dp[-1])