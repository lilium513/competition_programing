import math
import sys

N,W = map(int, sys.stdin.readline().split())

items= [list(map(int, sys.stdin.readline().split()) )for _ in range(N)]
s  =0
for i in range(N):
    s += items[i][1]
INF = 10 **15
dp = [[ INF for _ in range(s +1)] for _ in range(N + 1) ]
#dp[今何個目か][価値] = その時の重さの最小値 重さの最小値がW以下の中で価値最大を出力
dp[0][0] = 0

for j in range(N):  # j 個目の荷物で
    for i in range(s + 1): # 価値

        w,v = items[j]
        if i >= v:
        #遷移 d[j + 1][i] =  (d[j][i - v] + w ) 新しい荷物を選んだ場合
            dp[j + 1 ][i] = dp[j][i - v]  + w  # dp[j][i - w]  + v → j 個持ったところに、更に 価値v のitemが追加されて j+ 1になった
        dp[j + 1][i] =  min(dp[j + 1][i] ,dp[j][i]) #選ばなかった場合
ans = 0
for i in range(s + 1): #価値i
    for j in range(N + 1):  # j 個目の荷物で
        if dp[j][i] <= W:
            ans = max(i,ans)

print(ans)