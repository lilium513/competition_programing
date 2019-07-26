MOD = 10**9+7
l = input()
n = len(l)
dp = [    [0,0] for _ in range(n + 1)]
dp[0][0]  = 1
#dp[桁数][条件を満たすことが確定しているフラグ]
# 00 10 01

for i in range(1,n +1):
    # (dp[i][flag]のflag,dp[i-1][flag]のflag,i桁目の数字) で繊維は2**3の8通り
    dp[i][1] += dp[i - 1][1] * 3 # i桁目が (0,1) flag が 1 1
    #flag 0→1はない

    if l[i-1] == "1":
        dp[i][0] += dp[i -1][0] * 2 #1,0  or 0,1のときに相変わらず未定
        dp[i][1] += dp[i -1][0] # 0,0のときだけ確定させられる e.g. 101 10 のときに次に0が来れば確定 なので0,0
    else:
        dp[i][0] +=dp[i-1][0] # 0,0 の場合のみ
        # dp[i][1] への遷移は無し
    dp[i][0] %= MOD
    dp[i][1] %= MOD
ans = dp[-1][0] + dp[-1][1]
print(ans % MOD)
