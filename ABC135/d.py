
import sys

S =  sys.stdin.readline()[:-1]
l = len(S)
# S = S[::-1]
S = list(reversed(S))

dp =[[0 ] * 13 for _ in range(l + 1)]
kurai = 1
MOD = (10 ** 9) + 7
dp[0][0] = 1

for index in range(len(S)):
    c =S[index]

    if c == "?":
        for j in range(0,10):
            kurai %= 13
            temp = (j * kurai) % 13
            for i in range(13):
                dp[index+ 1][(temp + i) % 13] += (dp[index][i] )
                dp[index + 1][(temp + i) % 13] %= MOD
    else:
        kurai %= 13

        temp = (int(c) * kurai) % 13
        for i in range(13):
            dp[index + 1][(temp + i) % 13]  += (dp[index][i] )
            dp[index + 1][(temp + i) % 13] %= MOD
    kurai *= 10
print(dp[-1][5] )

