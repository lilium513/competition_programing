import itertools
import math
N = int(input())
di = {}
for i in range(N):
    di[i+1] = int(input())

flag = False
next = 1
for i in range(N):
    if next == 2:
        flag = True
        break
    next = di[next]

    # print(next)
if flag:
    print(i)
else:
    print(-1)