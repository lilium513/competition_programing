import itertools
from itertools import accumulate
N,Q =list(map(int,input().split(" ")))
mass = [0] * (N+2)
for _ in range(Q):
    l,r=list(map(int, input().split(" ")))
    mass[l] += 1
    mass[r+1] -=1
mass = list(accumulate(mass))
mass = list(map(lambda x:str(x%2),mass))
print("".join(mass[1:-1]))