def GCD( a,  b ):
    if b == 0:
        # print("--" * 10)
        return a
    else:
        # print(b)
        return GCD(b, a % b)

import math
N,M = list(map(int,input().split(" ")))
X = list(map(int,input().split(" ")))
X.sort()
diffs = []

if N >= M:
    print(0)
else:
    for i,x in enumerate(X[1:]):
        diff = abs(x-X[i])
        diffs.append(diff)
    diffs.sort()
    # print(diffs)

    if N == 1:
        print(sum(diffs))
    else:
        print(sum(diffs[:-(N-1)]))
