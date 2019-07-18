import itertools
import copy
N = int(input())
Xs = list(map(int,input().split(" ")))
XsOrigin = copy.deepcopy(Xs)
Xs.sort()
l = int(len(Xs)/2)
left = Xs[l-1]
right =Xs[l]
for i in XsOrigin:
    if i <=left:
        print(right)
    else:
        print(left)