import math
import sys
N,M =list(map(int,input().split(" ")))

S = input().split(" ")
T = input().split(" ")

dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][0] = 1
#dp[ s_ind][t_ind] → S の  s_ind文字目、Tの t_ind文字目までのLCS
for s_ind in range(N):
    for t_ind in range(M):
        if S[s_ind]  == T[t_ind]:
            dp[s_ind + 1][t_ind + 1] += dp[s_ind ][t_ind ] + 1   # AB "C"    と DQ "C" → AB まで とDQまでが dp[s_ind - 1][t_ind -1] 、それに各+1文字してdp[s_ind ][t_ind ] 、共通列の長さも+1

        dp[s_ind + 1][t_ind + 1]  += max( dp[s_ind + 1][t_ind + 1],dp[s_ind][t_ind])




print(  sum(dp[-1]))



