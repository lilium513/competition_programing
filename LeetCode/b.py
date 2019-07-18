N,K = list(map(int,input().split(" ")))
hs = list(map(int,input().split(" ")))
dp = [9999999999999] * N

dp[0] = 0
for i in range(1,N):
#ind → i-1 ~ i-stepLim -1   [i-stepLim -1:i]
    stepLim = min(K,i)
    dp[i] = min([d+abs(hs[i]-h) for d,h in zip(dp[i-stepLim:i],hs[i-stepLim:i])])
print(dp[-1])