

import math
N,Ma,Mb = map(int,input().split(" "))
drags = [list(map(int,input().split(" "))) for  _ in range(N)]
INF = 10 ** 9
lim = N* 10 + 1
dp = [[[ INF for i in range(lim)] for j in range(lim)] for _ in range(N+1)]
dp[0][0][0] = 0
for num in range( N ):
    a,b,c = drags[num]
    dp[num + 1][0][0] = 0
    for i in range(0,lim): #完成した液体の aの量
        for j in range(0,lim):# bの量
            dp[num + 1][i][j]  =  dp[num][i][j]
            if i - a >= 0 and j - b >= 0:
                dp[num + 1][i ][j ] = min(dp[num][i ][j ] ,dp[num][i -a ][j -b  ]  + c)

ans = INF
for i in range(1,41):
    MA = Ma * i
    MB = Mb * i
    if MA >= lim or MB >= lim:
        break
    ans = min(ans, dp[-1][MA][MB])
if ans == INF:
    ans = -1
print(ans)

