import itertools
from math import ceil
from decimal import Decimal

N = input()
N = int(N)
lasta,lastb = 1,1
temp = []
for _ in range(N):
    temp.append(list(map(int,input().split(" "))))


for hoge in temp:
    a,b = hoge
    diffa = ceil(Decimal(lasta)/Decimal(a))
    diffb = ceil(Decimal(lastb)/Decimal(b))
    diff = max(diffa,diffb)
    lasta,lastb = a*diff,b*diff
print(lasta+lastb)