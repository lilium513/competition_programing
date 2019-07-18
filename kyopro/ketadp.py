N = input()
l = len(N)
dp = [[i for i in [0,0]] for  _ in range( l + 1)]

# e.g 8456
dp[0][0] = 1


for i in range(0, l):
    for j in [1,0]: #未満フラグ → 立ってればなんでもOK、そうでないと制限がかかる
        lim = 9 if j == 1 else int(N[i])
        for d in range(0,lim + 1): #i + 1桁目 に加える数字
            flag = 0
            if j == 1 or (d < lim): # 未満フラグ
                flag = 1
            dp[i + 1][flag] += dp[i][j]
print(dp)

