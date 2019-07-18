

import math
N,Ma,Mb = map(int,input().split(" "))
drags = [list(map(int,input().split(" "))) for  _ in range(N)]
dps = [[0 for i in range(41)] for j in range(41)]
for drag in drags:
