import itertools
import copy
n = int(input())
As = list(map(int,input().split(" ")))

As.sort()
if As[-1] % 2 == 0:
    r = As[-1]//2
    l = As[-1] // 2
else:
    r = As[-1] // 2
    l = As[-1] -r

ans = 10e9
for a in As:
    if abs(a-r) < abs ( ans - r ):
        ans = a
    if abs(a-l) < abs ( ans - l ):
        ans = a

print(As[-1],ans)