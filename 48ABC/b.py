import itertools
import math
a,b,x  =list(map(int,input().split(" ")))
diva  = (a)//x
divb = (b )//x
ans = divb -diva
if a % x == 0 and b % x == 0:
    ans += 1

print(ans)