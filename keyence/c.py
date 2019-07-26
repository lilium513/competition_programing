import math
N = int(input())
As = list(map(int,input().split(" ")))
Bs = list(map(int,input().split(" ")))
over = []
under = []
for a,b in zip(As,Bs):
    if a < b:
        under.append(b-a)
    if a > b:
        over.append(a-b) #1個
#overの要素を幾つ使えばunderを包めるか
if len(under) == 0:
    print(0)
    exit()

over.sort(reverse=True)
under_sum = sum(under)
l = len(over)
for i in range(l):
    under_sum -= over[i]
    if under_sum  <= 0:
        break
if under_sum  > 0:
    print(-1)
else:
    print(i+ 1 + len(under)) #これは少なくとも全部書き換える
# +overで使った分の長さ