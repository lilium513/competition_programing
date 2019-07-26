import math
import sys

N,W = map(int, sys.stdin.readline().split())

items= (list(map(int, sys.stdin.readline().split()) )for _ in range(N))


dp = [[0 for _ in range(W+1)] for _ in range(N + 1) ]
#dp[今何個目か][重さ何キロ持つか] = その時の価値の最大値
dp[0][0] = 0

for i in range(W+1): #重さ i のときに得られる価値
    for j in range(N):  # j 個目の荷物で
        w,v = items[j]
        if i >= w: # w > i だと前提が破綻するので
            #遷移 d[j + 1][i] =  (d[j][i - w] + v ) 新しい荷物を選んだ場合
            dp[j + 1 ][i] = dp[j][i - w]  + v  # dp[j][i - w]  + v → j 個持ったところに、更に 価値v のitemが追加されて j+ 1になった
        dp[j + 1][i] =  max(dp[j + 1][i] ,dp[j][i]) #選ばなかった場合

print(dp[N][W])