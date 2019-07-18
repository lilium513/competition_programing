def GCD( a,  b ):
    if b == 0:
        # print("--" * 10)
        return a
    else:
        # print(b)
        return GCD(b, a % b)

import math
N,X = list(map(int,input().split(" ")))
xs = list(map(int,input().split(" ")))
xs = list(map(lambda x:abs(x-X),xs))
gcds = [xs[0]]
for i,x in enumerate(xs[1:]):
    gcds.append(GCD(gcds[i],x))
print(gcds[-1])

