import math
import sys

S = sys.stdin.readline()[:-1]
T = sys.stdin.readline()[:-1]
sl = len(S)
tl = len(T)
dp = [[0 for _ in range(tl + 1)] for _ in range(sl + 1)]

#dp[ s_ind][t_ind] → S の  s_ind文字目、Tの t_ind文字目までのLCS
ans = ""
for s_ind in range(sl):
    for t_ind in range(tl ):
        if S[s_ind]  == T[t_ind]:
            dp[s_ind + 1][t_ind + 1] = dp[s_ind ][t_ind ] + 1   # AB "C"    と DQ "C" → AB まで とDQまでが dp[s_ind - 1][t_ind -1] 、それに各+1文字してdp[s_ind ][t_ind ] 、共通列の長さも+1

        dp[s_ind + 1][t_ind + 1]  = max(dp[s_ind + 1][t_ind + 1],dp[s_ind + 1][t_ind  ],dp[s_ind][t_ind+ 1])

i = sl
j = tl
while i > 0 and j > 0:
    if dp[i][j] == dp[i][j- 1]:
        j -=1
    elif dp[i][j] == dp[i - 1][j]:
        i -=1
    else:
        ans = S[i -1 ] + ans
        i -=1
        j -=1


print(ans)



