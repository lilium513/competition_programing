import itertools
import math
N = int(input())
As = list(map(int,input().split(" ")))
ans = []
off = 0
if N%2 == 1:
    off = 1

for i in range(N-1,-1,-2):
    ans.append(As[i])
for i in range(off,N,2):
    ans.append(As[i])
ans = list(map(str,ans))
print(" ".join(ans))