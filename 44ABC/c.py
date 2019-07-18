
N,A = list(map(int,input().split(" ")))
nums = list(map(int,input().split(" ")))

dp = [[[0 for i in range(4000)]for j in range(51)]for k in range(51)]

# dp[i][j][k] → i枚のうちj枚を選んで 和が kになる組み合わせ
dp[0][0][0] = 1
for i in range(N):
    for j in range(N):
        for k in range(3000):
            if dp[i][j][k] != 0:
                dp[i+1][j][k] += dp[i][j][k]    #i枚目を選ばなかった世界線
                dp[i + 1][j + 1][k + nums[i]]  += dp[i][j][k]          #i枚目を選んだ世界線


ans = 0
for j in range(1,N+1):
    ans += dp[N][j][j*A]
print(ans)