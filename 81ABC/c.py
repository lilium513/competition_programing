import itertools
import math
N = input()
l = list(map(int,input().split(" ")))
av = sum(l)/len(l)
can1 = int(math.ceil(av))
can2 = int(math.floor(av))
ans1 = sum(list(map(lambda x:(x-can1)**2,l)))
ans2 = sum(list(map(lambda x:(x-can2)**2,l)))
print(min(ans2,ans1))