N = int(input())
hs = list(map(int,input().split(" ")))
dp = [0] * N

dp[0]=0
dp[1]= abs(hs[0]-hs[1]) 

for i in range(2,N):
    c1 = dp[i-1]+abs(hs[i]-hs[i-1])
    c2 = dp[i-2]+abs(hs[i]-hs[i-2])
    dp[i] = min(c1,c2)
print(dp[-1])