from datetime import datetime as dt
X,Y,Z,K = list(map(int,input().split(" ")))
As = list(map(int,input().split(" ")))
Bs = list(map(int,input().split(" ")))
Cs = list(map(int,input().split(" ")))

As.sort(reverse = True )
Bs.sort(reverse = True )

ABs = []
for a in As:
    for b in Bs:
        ABs.append(a + b)
ABs.sort(reverse = True)
upper = min(len(ABs),K)

ABs = ABs[:upper]
ans = []

for C in Cs:
    for AB in ABs:
        ans.append(AB+C)
ans.sort(reverse = True)
for i in range(K):
    print(ans[i])
