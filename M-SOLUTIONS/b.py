import itertools
import math
W,H,N  =list(map(int,input().split(" ")))
hoko = [0,W,0,H]
l = 0
r = W
ue = H
sita = 0

for _ in range(N):
    x,y,a=list(map(int, input().split(" ")))

    if a ==1:
      if l < x:
          l = x
    if a == 2:
        if r > x:
            r = x

    if a == 4:
        if ue > y:
            ue = y
    if a == 3:
        if sita < y:
            sita = y

if (r-l) < 0 and (ue-sita) < 0:
    print(0)
else:
    print(max(0,  (r-l) * (ue-sita)   ))