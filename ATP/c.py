import math
N = int(input())
days = []
temp = [list(map(int, input().split(" "))) for _ in range(N)]
days.extend(temp)


dp = [[-1 for _ in range(3)] for _ in range(N + 1) ]


dp[1] = days[0]

for d in range(1,N ):
    for a in range(3): #d+1日目にする活動
        cands = []
        for i in range(3):
            if i != a:
                cands.append(dp[d][i])

        dp[d+1][a] = max(cands) + days[d][a]

print(max(dp[-1]))