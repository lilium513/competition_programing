import itertools
import math
nums =list(map(int,input().split(" ")))
anss = []
for temp in  itertools.combinations(nums,3):
    anss.append(sum(temp))

anss = list(set(anss))
anss.sort()
print(anss[-3])